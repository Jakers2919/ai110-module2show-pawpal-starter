
from dataclasses import dataclass, field


@dataclass
class Task:
    """Represents a pet care task."""
    title: str
    duration_minutes: int
    priority: str
    scheduled_time: str = "08:00"
    frequency: str = "once"
    completed: bool = False

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
        """Return all tasks for this pet."""
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

    def generate_daily_plan(self, owner: Owner):
        """Create a daily plan based on priority and available time."""
        tasks = self.filter_tasks(owner.get_all_tasks())

        priority_order = {
            "high": 0,
            "medium": 1,
            "low": 2
        }

        tasks = sorted(
            tasks,
            key=lambda task: (
                priority_order.get(task.priority.lower(), 3),
                task.scheduled_time
            )
        )

        daily_plan = []
        minutes_used = 0

        for task in tasks:
            if minutes_used + task.duration_minutes <= self.available_minutes:
                daily_plan.append(task)
                minutes_used += task.duration_minutes

        return daily_plan

    def sort_by_time(self, tasks):
        """Sort tasks by their scheduled times."""
        return sorted(tasks, key=lambda task: task.scheduled_time)

    def filter_tasks(self, tasks):
        """Remove completed tasks from the schedule."""
        return [task for task in tasks if not task.completed]

    def detect_conflicts(self, tasks):
        """Placeholder for conflict detection in Phase 4."""
        return []

    def handle_recurring_tasks(self, tasks):
        """Placeholder for recurring tasks in Phase 4."""
        return []
