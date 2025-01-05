import random
import os
import sys

# -----------------------------
# CONFIGURABLE SETTINGS
# -----------------------------
MIN_TASKS = 2   # minimum number of tasks
MAX_TASKS = 6   # maximum number of tasks
LOG_FILE = "task_log.txt"

# If a log file doesn't exist, create one
if not os.path.exists(LOG_FILE):
    with open(LOG_FILE, 'w') as f:
        f.write("=== Task Completion Log ===\n\n")

def log_progress(message: str):
    """Append a timestamped message to the log file."""
    from datetime import datetime
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, 'a') as f:
        f.write(f"[{timestamp}] {message}\n")

def display_status(tasks_completed, target):
    """Display how many tasks are completed and how many are needed."""
    print(f"Tasks Completed: {tasks_completed} / {target}")

def main(show_status=False, target_changeable=False):
    """
    A command-line tool that:
    1. Displays how many tasks are needed before a LoL break.
    2. Allows the user to mark tasks as 'done'.
    3. Rewards the user (in theory) with a League match once target is reached.
    4. Resets the target and continues.
    """

    # -----------------------------
    # INITIALIZATION
    # -----------------------------
    # This variable holds how many tasks you must complete 
    # before you're allowed to play a League match.
    current_target = random.randint(MIN_TASKS, MAX_TASKS)

    tasks_completed = 0

    print("Welcome to the Task-Reward Tracker!")
    print(f"Your current target is {current_target} tasks before you can play a League match.\n")

    while True:
        print("Choose an option:")
        print("1) Mark a task as completed")
        print("2) Check current status")
        print("3) Reset the target manually (if needed)")
        print("4) Exit\n")
        
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == "1":
            tasks_completed += 1
            log_progress("Task completed.")
            
            if show_status:
                display_status(tasks_completed, current_target)
            
            # Check if tasks_completed meets the current target
            if tasks_completed >= current_target:
                print("\n*** Congratulations! You've earned a League of Legends match! ***")
                log_progress("Target reached. League match reward granted.")
                
                # Ask user if they are going to play or skip
                # (Skipping might make sense if user wants to store a 'token' for later, 
                #  but let's keep it simple.)
                
                play_now = input("Type 'play' to confirm you're going to play now, or press Enter to skip: ").strip().lower()
                if play_now == "play":
                    print("Launching League of Legends is up to you—this script won't do it automatically.")
                    print("Enjoy your break, then come back and continue your tasks!\n")
                else:
                    print("You chose not to play right now. You can still consider the reward 'banked.'\n")
                
                # Reset the tasks completed and pick a new target
                tasks_completed = 0
                new_target = random.randint(MIN_TASKS, MAX_TASKS)
                print(f"Your new target is: {new_target} tasks.\n")
                log_progress(f"New target set to {new_target} tasks.")
                
                current_target = new_target
                
        elif choice == "2":
            if show_status:
                display_status(tasks_completed, current_target)
            else:
                print("Display status is not enabled. Please enable it with --display-status.\n")
            
        elif choice == "3":
            if target_changeable: 


                # Manually reset the target in case user needs an adjustment
                new_target = input(f"Enter a new target number (current is {current_target}): ").strip()
                if new_target.isdigit():
                    current_target = int(new_target)
                    log_progress(f"Target manually reset to {current_target} tasks.")
                    print(f"Target updated to {current_target} tasks.\n")
                else:
                    print("Invalid input. Target not changed.\n")
                
            else:
                print("Target is not changeable. Please reset the target manually.\n")
                
        elif choice == "4":
            print("Exiting the program. Keep up the good work!")
            break
            
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":

    # Read command line arguments for display_status and target_changeable
    show_status = "--show-status" in sys.argv
    target_changeable = "--target-changeable" in sys.argv

    main(show_status=show_status, target_changeable=target_changeable)

