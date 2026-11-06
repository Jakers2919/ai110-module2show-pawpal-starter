# PawPal+ Project Reflection

## 1. System Design

### a. Initial design

My initial design for PawPal+ includes four main classes: Owner, Pet, Task, and Scheduler. I wanted to keep the system simple so each class has its own responsibility.

The Owner class manages the user's pets. The Pet class stores information about each pet and the tasks assigned to it. The Task class keeps track of activities like feeding, walking, and grooming, including their scheduled times and whether they are completed. The Scheduler class organizes the tasks and helps the owner see what needs to be done.

The three main actions I want users to perform are adding a pet, scheduling a task, and viewing their daily schedule. I think separating these responsibilities will make the code easier to understand and update.

### b. Design changes

After reviewing my initial design with Codex, I decided to keep the same four classes because each one already has a clear responsibility. Codex suggested having the scheduler explain why certain tasks get skipped and adding basic owner preferences. I decided to include those features during implementation instead of making the design more complicated with extra classes.

---

## 2. Scheduling Logic and Tradeoffs

### a. Constraints and priorities

My scheduler considers task priority, scheduled time, and how much time the owner has available. I made high-priority tasks come first because activities like feeding and walking are more important than optional tasks. The scheduler checks how long each task takes and skips tasks that would go over the available time.

After selecting the tasks, it sorts them by their scheduled times so the daily plan is easier to follow. It also detects overlapping tasks and supports daily or weekly recurring tasks.

### b. Tradeoffs

One tradeoff I made was prioritizing important tasks instead of always choosing the earliest tasks first. This means a lower-priority task might get skipped if there is not enough time available.

I think this makes sense because the main goal of PawPal+ is to help owners take care of their pets' most important needs. I also decided to warn users about overlapping tasks instead of automatically changing their scheduled times. This keeps the system simple and lets the owner decide how to handle conflicts.

---

## 3. AI Collaboration

### a. How you used AI

To be completed as I use AI to design, implement, and test the project.

### b. Judgment and verification

To be completed after reviewing and evaluating an AI suggestion.

---

## 4. Testing and Verification

### a. What you tested

To be completed during Phase 5 after running the automated tests.

### b. Confidence

To be completed after reviewing the test results.

---

## 5. Reflection

### a. What went well

To be completed after finishing the project.

### b. What you would improve

To be completed after evaluating the finished application.

### c. Key takeaway

To be completed after finishing the project.