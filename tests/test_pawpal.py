
from datetime import date, timedelta

from pawpal_system import Owner, Pet, Task, Scheduler


def test_mark_task_complete():
    """Test that a task can be completed."""
    task = Task("Morning walk", 30, "high")
    task.mark_complete()

    assert task.completed is True


def test_add_task_to_pet():
    """Test that a pet can receive tasks."""
    pet = Pet("Mochi", "dog")
    task = Task("Feeding", 10, "high")

    pet.add_task(task)

    assert len(pet.get_tasks()) == 1


def test_sort_tasks_by_time():
    """Test that tasks are sorted chronologically."""
    scheduler = Scheduler()

    tasks = [
        Task("Evening walk", 30, "medium", "18:00"),
        Task("Morning walk", 30, "high", "08:00"),
        Task("Feeding", 10, "high", "09:00"),
    ]

    sorted_tasks = scheduler.sort_by_time(tasks)

    assert [task.scheduled_time for task in sorted_tasks] == [
        "08:00", "09:00", "18:00"
    ]


def test_daily_recurring_task():
    """Test that daily tasks repeat the following day."""
    owner = Owner("Jordan")
    pet = Pet("Mochi", "dog")
    owner.add_pet(pet)

    task = Task(
        "Morning walk", 30, "high",
        scheduled_time="08:00",
        frequency="daily"
    )

    pet.add_task(task)
    task.mark_complete()

    scheduler = Scheduler()
    new_tasks = scheduler.handle_recurring_tasks(owner)

    assert len(new_tasks) == 1
    assert new_tasks[0].due_date == (
        date.today() + timedelta(days=1)
    ).isoformat()
    assert new_tasks[0].completed is False


def test_detect_conflicting_tasks():
    """Test that overlapping tasks are detected."""
    scheduler = Scheduler()

    tasks = [
        Task("Morning walk", 30, "high", "08:00"),
        Task("Feeding", 10, "high", "08:15"),
    ]

    conflicts = scheduler.detect_conflicts(tasks)

    assert len(conflicts) == 1
    assert conflicts[0][0].title == "Morning walk"
    assert conflicts[0][1].title == "Feeding"


def test_skip_tasks_over_time_limit():
    """Test that the scheduler respects available time."""
    owner = Owner("Jordan")
    pet = Pet("Mochi", "dog")
    owner.add_pet(pet)

    pet.add_task(Task("Morning walk", 30, "high", "08:00"))
    pet.add_task(Task("Playtime", 20, "low", "10:00"))

    scheduler = Scheduler(available_minutes=30)
    plan = scheduler.generate_daily_plan(owner)

    assert len(plan) == 1
    assert plan[0].title == "Morning walk"
    assert len(scheduler.skipped_tasks) == 1


def test_completed_tasks_are_filtered():
    """Test that completed tasks do not appear in the plan."""
    owner = Owner("Jordan")
    pet = Pet("Mochi", "dog")
    owner.add_pet(pet)

    task = Task("Feeding", 10, "high")
    pet.add_task(task)
    task.mark_complete()

    scheduler = Scheduler()
    plan = scheduler.generate_daily_plan(owner)

    assert len(plan) == 0
