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
- Use a Streamlit interface to manage pets and view schedules.

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
streamlit run app.py
```

The Streamlit app allows users to enter pet information, add care tasks, and generate a daily schedule. Advanced conflict warnings and recurring-task controls will be added to the interface during Phase 6.

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

Current test results:

```text
tests/test_pawpal.py .. [100%]
2 passed in 0.02s
```

The current tests verify that:

1. Marking a task complete updates its completion status.
2. Adding a task to a pet increases the number of tasks.

Additional tests for chronological sorting, recurring tasks, and conflict detection will be added during Phase 5.

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

## Demo Walkthrough

1. Launch the Streamlit application.
2. Enter the owner's name and add a pet.
3. Add care tasks with durations, priorities, and scheduled times.
4. Enter the amount of time available for pet care.
5. Click **Generate Schedule** to create a daily plan.
6. View the selected tasks in the schedule table.
7. Use the CLI demonstration to see conflict detection, skipped-task explanations, and recurring-task creation.

## Project Structure

- `app.py` — Streamlit user interface.
- `pawpal_system.py` — Main Python classes and scheduling algorithms.
- `main.py` — Command-line demonstration.
- `tests/test_pawpal.py` — Automated tests.
- `diagrams/uml.mmd` — UML class diagram.
- `reflection.md` — Project reflection and design decisions.
- `ai_interactions.md` — Optional AI collaboration log for stretch features.

## Future Improvements

Future improvements could include automatically resolving overlapping tasks, more detailed owner preferences, and better recurring-task controls in the Streamlit interface.