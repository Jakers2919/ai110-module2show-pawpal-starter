
import streamlit as st
from pawpal_system import Owner, Pet, Task, Scheduler

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")
st.write("Your personal pet care scheduling assistant.")

# Keep the owner and pets saved between Streamlit reruns.
if "owner" not in st.session_state:
    st.session_state.owner = Owner("Jordan")

if "scheduler" not in st.session_state:
    st.session_state.scheduler = Scheduler(available_minutes=480)

st.subheader("Owner Information")

owner_name = st.text_input(
    "Owner name",
    value=st.session_state.owner.name
)

st.session_state.owner.name = owner_name

st.divider()

st.subheader("Add a Pet")

with st.form("add_pet_form"):
    pet_name = st.text_input("Pet name")
    species = st.selectbox("Species", ["Dog", "Cat", "Other"])
    add_pet = st.form_submit_button("Add Pet")

    if add_pet:
        if pet_name.strip():
            existing = any(
                pet.name.lower() == pet_name.strip().lower()
                for pet in st.session_state.owner.pets
            )

            if existing:
                st.warning("A pet with that name already exists.")
            else:
                pet = Pet(name=pet_name.strip(), species=species)
                st.session_state.owner.add_pet(pet)
                st.success(f"{pet_name} was added!")
        else:
            st.warning("Please enter a pet name.")

if st.session_state.owner.pets:
    st.write("### Your Pets")

    for pet in st.session_state.owner.pets:
        st.write(f"🐾 {pet.name} ({pet.species})")
else:
    st.info("No pets added yet.")

st.divider()

st.subheader("Schedule a Task")

if st.session_state.owner.pets:
    with st.form("add_task_form"):
        selected_pet = st.selectbox(
            "Choose a pet",
            [pet.name for pet in st.session_state.owner.pets]
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
            if task_title.strip():
                task = Task(
                    title=task_title.strip(),
                    duration_minutes=int(duration),
                    priority=priority,
                    scheduled_time=scheduled_time.strftime("%H:%M"),
                    frequency=frequency
                )

                for pet in st.session_state.owner.pets:
                    if pet.name == selected_pet:
                        pet.add_task(task)
                        break

                st.success(f"{task_title} added for {selected_pet}!")
            else:
                st.warning("Please enter a task name.")
else:
    st.info("Add a pet before scheduling tasks.")

st.divider()

st.subheader("Today's Schedule")

available_minutes = st.number_input(
    "Available time today (minutes)",
    min_value=1,
    max_value=1440,
    value=480
)

if st.button("Generate Schedule"):
    st.session_state.scheduler.available_minutes = int(available_minutes)

    daily_plan = st.session_state.scheduler.generate_daily_plan(
        st.session_state.owner
    )

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
        st.write(f"Total scheduled time: {total_minutes} minutes")
        st.caption(
            "Tasks are selected by priority and available time. "
            "Advanced conflict detection and recurring-task handling "
            "will be added in Phase 4."
        )
    else:
        st.warning("No tasks available to schedule.")
