# ========= SE T21 - Compulsory Task ===========

# === importing libraries ===
from datetime import date

# === Initialising variables ===
username_list = []
password_list = []
break_while = False
task_count = 0
user_count = 0

# === Login Section ===

# Reading the username and password file (user.txt) and storing them into separate lists.
with open('user.txt', 'r') as user_file:
    for line in user_file:
        # Processing the line to make it easier to work with.
        line = line.strip()
        username_stored, password_stored = line.split(", ")

        username_list.append(username_stored)
        password_list.append(password_stored)

# Using a while loop to facilitate the login process. If a user is unsuccessful, they will be asked again.
while True:
    current_username = input("Please enter your username: ")
    password = input("Please enter your password: ")

    if current_username not in username_list:
        print("Sorry, that username is not recognised. Try again.")
        continue

    elif current_username in username_list and password not in password_list:
        print("Sorry, that password is not recognised. Try again.")
        continue

    # Note: a user will have the same index in username_list and password_list.
    for details_idx in range(len(username_list)):

        if current_username == username_list[details_idx] and password == password_list[details_idx]:
            print("\nYou have successfully logged in.\n")
            break_while = True
            break

    if break_while:
        break

# Presenting the menu to the user. If the admin is logged in, they will have access to a separate menu.
while True:
    if current_username == "admin":
        menu = input("Select one of the following options below:\n"
                     "r  - Registering a user\n"
                     "a  - Adding a task\n"
                     "va - View all tasks\n"
                     "vm - View my task\n"
                     "vs - View task statistics\n"
                     "e  - Exit\n"
                     "\nEnter here: ").lower()

    else:
        menu = input("Select one of the following options below:\n"
                     "r  - Registering a user\n"
                     "a  - Adding a task\n"
                     "va - View all tasks\n"
                     "vm - View my task\n"
                     "e  - Exit\n"
                     "\nEnter here: ").lower()

    # === Register a new user section ===
    # In this section, only the admin has permission to add a new user. They will be written to the 'user.txt' file.
    if menu == 'r':

        if current_username == "admin":
            while True:
                new_username = input("Please enter the username you'd like to register: ")
                new_password = input("Please enter their new password: ")
                new_password_confirm = input("Please confirm their new password: ")

                if new_password == new_password_confirm:

                    with open('user.txt', 'a') as user_file:
                        user_file.write(f"\n{new_username}, {new_password}")
                        print(f"\nYou have successfully registered a new user."
                              "Taking you back to the menu shortly...\n")
                        break

                elif new_password != new_password_confirm:
                    print("Your passwords do not match. Try again.")
                    continue

        else:
            print("\nOnly the admin has privileges to do this. Taking you back to the main menu shortly...\n")

    # === Add a new task section ===
    # This section allows the user to add a new task. It will be written to the 'task.txt' file.
    elif menu == 'a':
        username = input("Please enter the username of the person whom the task is assigned to: ")
        title = input("Please enter the title of the task: ")
        description = input("Please enter the description of the task: ")
        date_due = input("Please enter the due date of the task (DD MMM YYYY): ")
        date_today = date.today()
        date_today = date_today.strftime("%d %b %Y")

        with open('tasks.txt', 'a') as task_file:
            task_file.write(f"\n{username}, {title}, {description}, {date_due}, {date_today}, No")

        print(f"\nYou have successfully added a task. Taking you back to the menu shortly...\n")

    # === View all task section ===
    # This section allows the user to view all tasks and their details.
    elif menu == 'va':
        print("\nTask List (ALL):-\n")

        with open('tasks.txt', 'r') as task_file:
            for line in task_file:
                # Processing the line to make it easier to work with.
                line = line.strip()
                line = line.split(", ")

                print(f"Task: {line[1]}\n"
                      f"Assigned to: {line[0]}\n"
                      f"Date assigned: {line[4]}\n"
                      f"Due date: {line[3]}\n"
                      f"Task complete?: {line[5]}\n"
                      f"Description:\n"
                      f"{line[2]}\n"
                      f"-------------------------------------------------------")

        print("\nYou have viewed all tasks. Taking you back to the menu shortly...\n")

    # === View my task section ===
    # This section allows the user to view all of their own tasks and their details.
    elif menu == 'vm':
        print("\nYour Task List:-\n")

        with open('tasks.txt', 'r') as task_file:
            for line in task_file:

                # Processing the line to make it easier to work with.
                line = line.strip()
                line = line.split(", ")

                if line[0] == current_username:
                    print(f"Task: {line[1]}\n"
                          f"Assigned to: {line[0]}\n"
                          f"Date assigned: {line[4]}\n"
                          f"Due date: {line[3]}\n"
                          f"Task complete?: {line[5]}\n"
                          f"Description:\n"
                          f"{line[2]}\n"
                          f"-------------------------------------------------------")

        print("\nYou have viewed all tasks. Tacking you back to the menu shortly...\n")

    # === View statistics section ===
    # This section allows the admin to view the task statistics.

    elif menu == 'vs' and current_username == "admin":
        with open('tasks.txt', 'r') as task_file:
            for line in task_file:
                task_count += 1

        with open('user.txt', 'r') as user_file:
            for line in user_file:
                user_count += 1

        print("\nTask Statistics:-\n"
              f"Total number of tasks: {task_count}\n"
              f"Total number of users: {user_count}\n"
              f"-------------------------------------------------------"
              "\nYou have viewed the statistics. Tacking you back to the menu shortly...\n")

        # Resetting the counts incase the user wants to re-enter this section more than once.
        task_count = 0
        user_count = 0

    elif menu == 'e':
        print("\nYou have successfully exited the task manager. Goodbye!!!")
        exit()

    else:
        print("\nYour input is not recognised. Please Try again.\n")
