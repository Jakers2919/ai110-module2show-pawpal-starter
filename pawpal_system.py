
from dataclasses import dataclass, field
from datetime import datetime, timedelta


@dataclass
class Task:
    """Represents a pet care task."""
    title: str
    duration_minutes: int
    priority: str
    scheduled_time: str = "08:00"
    frequency: str = "once"
    completed: bool = False
    due_date: str = field(
        default_factory=lambda: datetime.now().date().isoformat()
    )

    def mark_complete(self):
        """Mark this task as completed."""
        self.completed = True


@dataclass
class Pet:
    """Stores pet information and care tasks."""
    name: str
    species: str
    tasks: list[Task] = field(default_factory=list)

    def add_task(self, task: Task):
        """Add a care task to this pet."""
        self.tasks.append(task)

    def get_tasks(self):
        """Return the pet's tasks."""
        return self.tasks


class Owner:
    """Represents a pet owner."""

    def __init__(self, name: str):
        self.name = name
        self.pets: list[Pet] = []

    def add_pet(self, pet: Pet):
        """Add a pet to the owner."""
        self.pets.append(pet)

    def get_all_tasks(self):
        """Return tasks from all owned pets."""
        all_tasks = []

        for pet in self.pets:
            all_tasks.extend(pet.get_tasks())

        return all_tasks


class Scheduler:
    """Organizes pet care tasks into a daily plan."""

    def __init__(self, available_minutes: int = 480):
        self.available_minutes = available_minutes
        self.skipped_tasks = []
        self.conflicts = []

    def sort_by_time(self, tasks):
        """Sort tasks chronologically."""
        return sorted(
            tasks,
            key=lambda task: datetime.strptime(
                task.scheduled_time, "%H:%M"
            )
        )

    def filter_tasks(self, tasks):
        """Return incomplete tasks due today."""
        today = datetime.now().date().isoformat()

        return [
            task for task in tasks
            if not task.completed and task.due_date == today
        ]

    def detect_conflicts(self, tasks):
        """Find overlapping tasks."""
        conflicts = []
        ordered = self.sort_by_time(tasks)

        for i, first in enumerate(ordered):
            first_start = datetime.strptime(
                first.scheduled_time, "%H:%M"
            )
            first_end = first_start + timedelta(
                minutes=first.duration_minutes
            )

            for second in ordered[i + 1:]:
                second_start = datetime.strptime(
                    second.scheduled_time, "%H:%M"
                )

                if second_start >= first_end:
                    break

                conflicts.append((first, second))

        return conflicts

    def generate_daily_plan(self, owner: Owner):
        """Select tasks by priority and display them by time."""
        tasks = self.filter_tasks(owner.get_all_tasks())

        priority_order = {
            "high": 0,
            "medium": 1,
            "low": 2
        }

        prioritized = sorted(
            tasks,
            key=lambda task: (
                priority_order.get(task.priority.lower(), 3),
                task.scheduled_time
            )
        )

        selected = []
        self.skipped_tasks = []
        minutes_used = 0

        for task in prioritized:
            if minutes_used + task.duration_minutes <= self.available_minutes:
                selected.append(task)
                minutes_used += task.duration_minutes
            else:
                self.skipped_tasks.append(
                    (task, "Exceeds available time")
                )

        daily_plan = self.sort_by_time(selected)
        self.conflicts = self.detect_conflicts(daily_plan)

        return daily_plan

    def handle_recurring_tasks(self, owner: Owner):
        """Create the next occurrence of completed recurring tasks."""
        new_tasks = []

        for pet in owner.pets:
            for task in list(pet.tasks):
                if not task.completed:
                    continue

                if task.frequency not in ("daily", "weekly"):
                    continue

                current_date = datetime.strptime(
                    task.due_date, "%Y-%m-%d"
                ).date()

                days = 1 if task.frequency == "daily" else 7
                next_date = current_date + timedelta(days=days)

                new_task = Task(
                    title=task.title,
                    duration_minutes=task.duration_minutes,
                    priority=task.priority,
                    scheduled_time=task.scheduled_time,
                    frequency=task.frequency,
                    due_date=next_date.isoformat()
                )

                pet.add_task(new_task)
                new_tasks.append(new_task)

                # Prevent creating the same recurrence twice.
                task.frequency = "once"

        return new_tasks
