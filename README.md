
# PawPal+ (Module 2 Project)

PawPal+ is a pet care scheduling app built with Python and Streamlit. It helps pet owners organize daily activities like feeding, walking, grooming, and playtime.

## Scenario

A busy pet owner needs help staying consistent with pet care. PawPal+ helps users:

- Track pet care tasks for multiple pets.
- Consider available time and task priorities.
- Generate a daily pet care schedule.
- Identify scheduling conflicts.
- Manage recurring tasks.

## Features

- Add pets and assign care tasks.
- Set task durations, priorities, and scheduled times.
- Generate a daily schedule based on available time.
- Prioritize important tasks when time is limited.
- Display selected tasks in chronological order.
- Skip completed tasks and tasks that exceed available time.
- Detect overlapping tasks and display conflict warnings.
- Support daily and weekly recurring tasks.
- Mark tasks complete through the Streamlit interface.
- Create the next occurrence of completed recurring tasks.
- Display skipped tasks and explain why they were skipped.
- Manage pets and tasks using a Streamlit interface.

## Getting Started

### Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Run the CLI Demo

```bash
python3 main.py
```

### Run the Streamlit App

```bash
python3 -m streamlit run app.py
```

The Streamlit app allows users to add pets, schedule care tasks, and generate daily schedules. It also displays scheduling conflicts, explains skipped tasks, and provides buttons to mark tasks complete. Completed recurring tasks can create their next occurrence.

## Sample Output

The following example comes from running `python3 main.py` after implementing smarter scheduling.

```text
PawPal+ Daily Schedule
Owner: Jordan

Total scheduled tasks: 4

Scheduling Conflicts:
WARNING: Morning walk overlaps with Feeding

Skipped Tasks:
Playtime: Exceeds available time

Recurring Task Demo:
Created next occurrence: Morning walk on 2026-11-07
```

The scheduler chooses tasks based on priority and available time, then displays them in chronological order. It also identifies conflicts and explains why tasks were skipped.

## Testing PawPal+

Run the automated tests using:

```bash
python3 -m pytest
```

### Test Results

The following results were recorded during Phase 5:

```text
tests/test_pawpal.py ....... [100%]
7 passed in 0.04s
```

All seven automated tests passed.

### What I Tested

1. **Task completion:** Verified that marking a task complete updates its completion status.
2. **Adding tasks:** Verified that adding a task to a pet increases the number of tasks.
3. **Chronological sorting:** Verified that tasks are sorted by their scheduled times.
4. **Recurring tasks:** Verified that completing a daily recurring task creates another task for the following day.
5. **Conflict detection:** Verified that overlapping tasks are identified.
6. **Available time:** Verified that tasks exceeding the available time are skipped.
7. **Completed task filtering:** Verified that completed tasks do not appear in the daily schedule.

### Confidence Level

**4 out of 5 stars**

I feel confident that the main scheduling features work because all seven automated tests passed. I also ran the CLI demonstration to check that the scheduler detects overlapping tasks, skips tasks when there is not enough time, and creates recurring tasks.

I tested the Streamlit interface by adding a pet, scheduling two overlapping tasks, and generating a daily schedule. The app displayed both tasks and correctly warned that their times overlapped.

If I had more time, I would add tests for weekly recurring tasks, invalid time inputs, and tasks that overlap across midnight.

## Smarter Scheduling

PawPal+ uses several scheduling methods to organize daily pet care tasks.

| Feature | Method(s) | Notes |
|---------|-----------|-------|
| Task sorting | `sort_by_time()` | Sorts selected tasks by scheduled time |
| Filtering | `filter_tasks()` | Excludes completed tasks and tasks not due today |
| Priority scheduling | `generate_daily_plan()` | Selects higher-priority tasks first |
| Available time | `generate_daily_plan()` | Skips tasks that exceed the daily time limit |
| Conflict handling | `detect_conflicts()` | Detects overlapping task times |
| Recurring tasks | `handle_recurring_tasks()` | Creates the next occurrence of completed daily or weekly tasks |

### Scheduling Decisions

The scheduler prioritizes high-priority tasks before medium- and low-priority tasks. It checks whether each task fits within the owner's available time.

Once tasks are selected, they are sorted by scheduled time so the daily schedule is easier to follow.

When two tasks overlap, the scheduler records a conflict rather than automatically changing their times. This lets the owner decide how to handle the situation.

For recurring tasks, the scheduler creates a new task for the next day or week after the current task is completed and recurrence processing is run.

## Streamlit Interface

The Streamlit interface includes the following sections:

### Owner Information

Users can enter their name to personalize the application.

### Add a Pet

Users can add pets by entering a name and selecting a species. The app prevents duplicate pet names.

### Schedule a Task

Users can create tasks with:

- Pet selection.
- Task name.
- Duration in minutes.
- Priority (high, medium, or low).
- Scheduled time.
- Frequency (once, daily, or weekly).

### Today's Schedule

Users can enter their available time and generate a schedule.

The app displays:

- Scheduled tasks in chronological order.
- Task durations, priorities, and frequencies.
- Total scheduled tasks and minutes.
- Warnings for overlapping tasks.
- Explanations for skipped tasks.
- Buttons to mark tasks complete.

## Demo Walkthrough

1. Launch the Streamlit application.
2. Enter the owner's name.
3. Add a pet named Mochi.
4. Add a Morning walk task at 08:15 for 10 minutes.
5. Add a Feeding task at 08:15 for 20 minutes.
6. Set the available time to 480 minutes.
7. Click **Generate Schedule**.
8. View both tasks in the daily schedule.
9. Check the Scheduling Conflicts section for the overlap warning.
10. Use the task completion buttons to mark finished tasks.
11. Use the CLI demonstration to see skipped-task explanations and recurring-task creation.

### Example Conflict Warning

```text
Morning walk overlaps with Feeding.
Consider changing one of their times.
```

This warning was successfully displayed during Streamlit testing.

## Project Structure

- `app.py` — Streamlit user interface.
- `pawpal_system.py` — Main Python classes and scheduling algorithms.
- `main.py` — Command-line demonstration.
- `tests/test_pawpal.py` — Automated tests.
- `diagrams/uml.mmd` — Initial UML class diagram.
- `diagrams/uml_final.mmd` — Final UML class diagram showing the completed scheduling system.
- `reflection.md` — Project reflection and design decisions.
- `ai_interactions.md` — Optional AI collaboration log for stretch features.

## Design Improvements

The original UML diagram included four main classes: Owner, Pet, Task, and Scheduler.

The final design kept these four classes while adding scheduling functionality.

Important improvements include:

- Due dates for tasks.
- Priority-based scheduling.
- Available-time limits.
- Conflict detection.
- Skipped-task explanations.
- Daily and weekly recurrence handling.
- Task completion tracking.

Keeping the same four classes helped make the system easier to understand and maintain.

## Future Improvements

Future improvements could include:

- Automatically resolving overlapping tasks.
- More detailed owner preferences.
- Editing and deleting existing tasks.
- Saving pets and tasks permanently between application restarts.
- More flexible recurring-task controls.
- Additional tests for unusual scheduling situations.

PawPal+ demonstrates how object-oriented programming, scheduling algorithms, automated testing, and a Streamlit interface can work together to create a practical pet care application.
