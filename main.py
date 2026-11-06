
from pawpal_system import Owner, Pet, Task, Scheduler


def main():
    """Demonstrate PawPal+ smarter scheduling."""

    owner = Owner("Jordan")

    dog = Pet("Mochi", "Dog")
    cat = Pet("Luna", "Cat")

    owner.add_pet(dog)
    owner.add_pet(cat)

    # Add tasks out of chronological order.
    dog.add_task(Task("Evening walk", 30, "medium", "18:00"))
    dog.add_task(Task("Morning walk", 30, "high", "08:00", "daily"))
    cat.add_task(Task("Feeding", 10, "high", "08:00", "daily"))
    cat.add_task(Task("Playtime", 20, "low", "14:00"))
    cat.add_task(Task("Grooming", 15, "medium", "10:00"))

    scheduler = Scheduler(available_minutes=90)
    daily_plan = scheduler.generate_daily_plan(owner)

    print("PawPal+ Daily Schedule")
    print(f"Owner: {owner.name}")
    print("-" * 45)

    for task in daily_plan:
        print(
            f"{task.scheduled_time} - {task.title} "
            f"({task.duration_minutes} min) "
            f"[priority: {task.priority}]"
        )

    print("-" * 45)
    print(f"Total scheduled tasks: {len(daily_plan)}")

    print("\nScheduling Conflicts:")
    if scheduler.conflicts:
        for first, second in scheduler.conflicts:
            print(f"WARNING: {first.title} overlaps with {second.title}")
    else:
        print("No conflicts detected.")

    print("\nSkipped Tasks:")
    if scheduler.skipped_tasks:
        for task, reason in scheduler.skipped_tasks:
            print(f"{task.title}: {reason}")
    else:
        print("No tasks skipped.")

    print("\nRecurring Task Demo:")
    recurring_task = dog.tasks[1]
    recurring_task.mark_complete()

    new_tasks = scheduler.handle_recurring_tasks(owner)

    for task in new_tasks:
        print(
            f"Created next occurrence: {task.title} "
            f"on {task.due_date}"
        )


if __name__ == "__main__":
    main()
