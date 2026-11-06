
from pawpal_system import Owner, Pet, Task, Scheduler


def main():
    """Demonstrate the PawPal+ scheduling system."""

    owner = Owner("Jordan")

    dog = Pet("Mochi", "Dog")
    cat = Pet("Luna", "Cat")

    owner.add_pet(dog)
    owner.add_pet(cat)

    dog.add_task(Task("Morning walk", 30, "high", "08:00"))
    dog.add_task(Task("Feeding", 10, "high", "09:00"))
    cat.add_task(Task("Playtime", 20, "medium", "10:00"))
    cat.add_task(Task("Grooming", 15, "low", "14:00"))

    scheduler = Scheduler(available_minutes=120)
    daily_plan = scheduler.generate_daily_plan(owner)

    print("🐾 PawPal+ Daily Schedule")
    print(f"Owner: {owner.name}")
    print("-" * 35)

    for task in daily_plan:
        print(
            f"{task.scheduled_time} — {task.title} "
            f"({task.duration_minutes} min) "
            f"[priority: {task.priority}]"
        )

    print("-" * 35)
    print(f"Total tasks scheduled: {len(daily_plan)}")


if __name__ == "__main__":
    main()
