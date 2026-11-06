
from pawpal_system import Task, Pet


def test_mark_task_complete():
    """Check that marking a task complete updates its status."""
    task = Task(
        title="Morning walk",
        duration_minutes=30,
        priority="high"
    )

    assert task.completed is False

    task.mark_complete()

    assert task.completed is True


def test_add_task_to_pet():
    """Check that adding a task increases the pet's task count."""
    pet = Pet(name="Mochi", species="Dog")

    task = Task(
        title="Feeding",
        duration_minutes=10,
        priority="high"
    )

    assert len(pet.tasks) == 0

    pet.add_task(task)

    assert len(pet.tasks) == 1
    assert pet.tasks[0].title == "Feeding"
