# PawPal+ Project Reflection

## 1. System Design

### a. Initial design

My initial design for PawPal+ includes four main classes: Owner, Pet, Task, and Scheduler. I wanted to keep the system simple so each class has its own responsibility.

The Owner class manages the user's pets. The Pet class stores information about each pet and the tasks assigned to it. The Task class keeps track of activities like feeding, walking, and grooming, including their scheduled times and whether they are completed. The Scheduler class organizes the tasks and helps the owner see what needs to be done.

The three main actions I want users to perform are adding a pet, scheduling a task, and viewing their daily schedule. I think separating these responsibilities will make the code easier to understand and update.

### b. Design changes

After reviewing my initial design with Codex, I decided to keep the same four classes because each one already has a clear responsibility. Codex suggested having the scheduler explain why certain tasks get skipped and adding basic owner preferences.

I decided to focus on explaining skipped tasks and improving the scheduling logic instead of adding more classes or making the design too complicated. My final UML diagram shows the additional features while keeping the original class structure.

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

I used ChatGPT and Codex to help me design, build, and test PawPal+. At the beginning, I used AI to help organize my ideas and create a UML diagram showing how the four main classes would work together.

During implementation, I used AI to help write the Python classes, connect the scheduling system to Streamlit, and improve the scheduling logic. It also helped me create automated tests and understand how to check whether the features were working correctly.

I used Codex in VS Code to review my initial design and get suggestions for improvements. One suggestion was to make the scheduler explain why tasks were skipped, which I included in my final implementation.

### b. Judgment and verification

I did not want to rely only on AI-generated code without checking whether it worked. After making changes, I ran the program and tested the features myself.

For example, I used the CLI demonstration to check that the scheduler detected overlapping tasks, skipped tasks when there was not enough time, and created recurring tasks. I also ran seven automated tests, and all of them passed.

I tested the Streamlit interface by adding a pet named Mochi and creating two tasks scheduled for the same time. The application displayed both tasks and correctly warned me that they overlapped.

I also decided not to automatically change overlapping task times because I thought it would be better for the pet owner to make that decision. This helped me keep the application simple while still providing useful warnings.

---

## 4. Testing and Verification

### a. What you tested

I created seven automated tests to make sure the main features of PawPal+ work correctly. I tested adding tasks to pets, marking tasks as completed, sorting tasks by time, and making sure completed tasks are not included in the daily schedule.

I also tested whether the scheduler respects the owner's available time, detects overlapping tasks, and creates a new task when a daily recurring task is completed.

These tests were important because I wanted to make sure the schedule was accurate and that the app could handle common situations without errors. All seven tests passed.

I also tested the Streamlit application by adding a pet, creating overlapping tasks, and generating a schedule. The application successfully displayed the tasks and showed a scheduling conflict warning.

### b. Confidence

I would rate my confidence in the scheduler a 4 out of 5. All seven automated tests passed, and the CLI demonstration successfully showed conflict detection, skipped tasks, and recurring tasks.

I think the main features work well, but there are still some edge cases I could test. If I had more time, I would test weekly recurring tasks, invalid scheduled times, and tasks that overlap across midnight.

---

## 5. Reflection

### a. What went well

One thing that went well was organizing the project into separate classes. Having Owner, Pet, Task, and Scheduler made it easier to understand what each part of the program was responsible for.

I also think the scheduling logic turned out well. The program can prioritize important tasks, detect conflicts, and explain why certain tasks are skipped. I was happy that all seven automated tests passed and that I was able to connect the Python code to a working Streamlit interface.

Another thing that went well was using AI to help troubleshoot and improve the project while checking the results myself.

### b. What you would improve

If I had more time, I would add a way for users to edit or delete tasks directly in the Streamlit application. I would also improve the recurring-task system so users could manage future tasks more easily.

Another improvement would be saving pets and tasks permanently. Right now, the app uses Streamlit session state, so the information can reset when the application restarts.

I would also add more automated tests for unusual scheduling situations and improve how the app handles overlapping tasks.

### c. Key takeaway

My biggest takeaway from this project was learning how to turn an object-oriented design into a working application. I started with a UML diagram, built the Python classes, added scheduling features, and connected everything to a Streamlit interface.

I also learned that AI can be useful for writing code, reviewing designs, and finding possible improvements, but it is still important to test the results instead of assuming everything works.

Overall, this project helped me get more comfortable with Python, object-oriented programming, automated testing, and building an application with multiple connected parts.