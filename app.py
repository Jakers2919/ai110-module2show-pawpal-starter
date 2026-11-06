
import streamlit as st
from pawpal_system import Owner, Pet, Task, Scheduler

st.set_page_config(
    page_title="PawPal+",
    page_icon="🐾",
    layout="centered"
)

st.title("🐾 PawPal+")
st.write("Your personal pet care scheduling assistant.")

# Save data between Streamlit reruns.
if "owner" not in st.session_state:
    st.session_state.owner = Owner("Jordan")

if "scheduler" not in st.session_state:
    st.session_state.scheduler = Scheduler(available_minutes=480)

owner = st.session_state.owner
scheduler = st.session_state.scheduler

# Owner information
st.subheader("Owner Information")

owner.name = st.text_input("Owner name", value=owner.name)

st.divider()

# Add pets
st.subheader("Add a Pet")

with st.form("add_pet_form"):
    pet_name = st.text_input("Pet name")
    species = st.selectbox("Species", ["Dog", "Cat", "Other"])
    add_pet = st.form_submit_button("Add Pet")

    if add_pet:
        if not pet_name.strip():
            st.warning("Please enter a pet name.")
        elif any(
            pet.name.lower() == pet_name.strip().lower()
            for pet in owner.pets
        ):
            st.warning("A pet with that name already exists.")
        else:
            owner.add_pet(Pet(pet_name.strip(), species))
            st.success(f"{pet_name} was added!")

if owner.pets:
    st.write("### Your Pets")
    for pet in owner.pets:
        st.write(f"🐾 {pet.name} ({pet.species})")
else:
    st.info("No pets added yet.")

st.divider()

# Add tasks
st.subheader("Schedule a Task")

if owner.pets:
    with st.form("add_task_form"):
        selected_pet = st.selectbox(
            "Choose a pet",
            [pet.name for pet in owner.pets]
        )

        task_title = st.text_input("Task name")

        duration = st.number_input(
            "Duration (minutes)",
            min_value=1,
            max_value=240,
            value=20
        )

        priority = st.selectbox(
            "Priority",
            ["high", "medium", "low"]
        )

        scheduled_time = st.time_input("Scheduled time")

        frequency = st.selectbox(
            "Frequency",
            ["once", "daily", "weekly"]
        )

        add_task = st.form_submit_button("Add Task")

        if add_task:
            if not task_title.strip():
                st.warning("Please enter a task name.")
            else:
                task = Task(
                    title=task_title.strip(),
                    duration_minutes=int(duration),
                    priority=priority,
                    scheduled_time=scheduled_time.strftime("%H:%M"),
                    frequency=frequency
                )

                for pet in owner.pets:
                    if pet.name == selected_pet:
                        pet.add_task(task)
                        break

                st.success(
                    f"{task_title} added for {selected_pet}!"
                )
else:
    st.info("Add a pet before scheduling tasks.")

st.divider()

# Daily schedule
st.subheader("Today's Schedule")

available_minutes = st.number_input(
    "Available time today (minutes)",
    min_value=1,
    max_value=1440,
    value=480
)

if st.button("Generate Schedule"):
    scheduler.available_minutes = int(available_minutes)
    st.session_state.show_schedule = True

if st.session_state.get("show_schedule", False):
    daily_plan = scheduler.generate_daily_plan(owner)

    if daily_plan:
        schedule_data = []

        for task in daily_plan:
            schedule_data.append({
                "Time": task.scheduled_time,
                "Task": task.title,
                "Duration": f"{task.duration_minutes} min",
                "Priority": task.priority,
                "Frequency": task.frequency
            })

        st.success("Your daily schedule is ready!")
        st.table(schedule_data)

        total_minutes = sum(
            task.duration_minutes for task in daily_plan
        )

        st.write(f"Total tasks: {len(daily_plan)}")
        st.write(
            f"Total scheduled time: {total_minutes} minutes"
        )

        st.caption(
            "Tasks are selected by priority and available time, "
            "then displayed in chronological order."
        )

        # Conflict warnings
        if scheduler.conflicts:
            st.subheader("Scheduling Conflicts")

            for first, second in scheduler.conflicts:
                st.warning(
                    f"{first.title} overlaps with {second.title}. "
                    "Consider changing one of their times."
                )
        else:
            st.success("No scheduling conflicts detected.")

        # Mark tasks complete
        st.subheader("Complete Tasks")

        for index, task in enumerate(daily_plan):
            if st.button(
                f"Mark {task.title} at {task.scheduled_time} Complete",
                key=f"complete_{id(task)}"
            ):
                task.mark_complete()

                new_tasks = scheduler.handle_recurring_tasks(owner)

                st.success(f"{task.title} marked complete!")

                for new_task in new_tasks:
                    st.info(
                        f"Next {new_task.title} scheduled "
                        f"for {new_task.due_date}."
                    )

                st.rerun()
    else:
        st.info("No tasks available to schedule today.")

    # Explain skipped tasks
    if scheduler.skipped_tasks:
        st.subheader("Skipped Tasks")

        for task, reason in scheduler.skipped_tasks:
            st.warning(f"{task.title}: {reason}")

st.divider()

st.caption("PawPal+ | CodePath Module 2 Project")
