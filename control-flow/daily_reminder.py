#!/usr/bin/env python3

# Prompt the user for task details
task = input("Enter your task: ").strip()
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# Process the task based on priority and time sensitivity
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task."
    case "medium":
        reminder = f"'{task}' is a medium priority task."
    case "low":
        reminder = f"'{task}' is a low priority task."
    case _:
        reminder = "Invalid priority level provided."

if time_bound == "yes" and "Invalid" not in reminder:
    reminder += " that requires immediate attention today!"
elif "Invalid" not in reminder:
    reminder += " Consider completing it when you have free time."

# Print the customized reminder
print(reminder)

