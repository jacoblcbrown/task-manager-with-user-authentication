# ========= SE T21 - Compulsory Task ===========

# === Importing libraries ===
from datetime import date
from datetime import datetime


# === Functions ===
# == Function to register new users ==
def reg_user():

    # Only the admin has permissions.
    if current_username == "admin":
        while True:
            new_username = input("Please enter the username you'd like to register: ")

            if new_username in user_info:
                print(f"\nThis user already exists. Try a new username.\n")
                continue

            else:
                # Confirming the new password.
                new_password = input("Please enter their new password: ")
                new_password_confirm = input("Please confirm their new password: ")

                if new_password == new_password_confirm:

                    with open('user.txt', 'a') as user_file:
                        user_file.write(f"\n{new_username}, {new_password}")
                        print("\nYou have successfully registered a new user. "
                              "Taking you back to the menu shortly...\n")
                        break

                elif new_password != new_password_confirm:
                    print("Your passwords do not match. Try again.\n")
                    continue

    else:
        print("\nOnly the admin has privileges to do this. Taking you back to the main menu shortly...\n")

    user_info_update()


# == Function to add new tasks ==
def add_task():

    # Requesting/assigning task information.
    username = input("Please enter the username of the person whom the task is assigned to: ")
    title = input("Please enter the title of the task: ")
    description = input("Please enter the description of the task: ")
    date_due = input("Please enter the due date of the task (DD Mmm YYYY): ")

    date_today = date.today()
    date_today = date_today.strftime("%d %b %Y")

    # Appending to task text file.
    with open('tasks.txt', 'a') as task_file:
        task_file.write(f"\n{username}, {title}, {description}, {date_today}, {date_due}, No")

    print(f"\nYou have successfully added a task. Taking you back to the menu shortly...\n")


#  == Function to view all tasks ==
def view_all():

    print("\nTask List (ALL):-\n")

    with open('tasks.txt', 'r') as task_file:

        # Initialising the counter at '1' so that the task dictionary is 'one'-indexed.
        task_count = 1

        for line in task_file:
            # Processing the line to make it easier to work with.
            line = line.strip()
            line = line.split(", ")

            # Displaying the task information.
            print(f"\033[1mTASK #{task_count}\033[0m\n"
                  f"Task: {line[1]}\n"
                  f"Assigned to: {line[0]}\n"
                  f"Date assigned: {line[3]}\n"
                  f"Due date: {line[4]}\n"
                  f"Task complete?: {line[5]}\n"
                  f"Description:\n"
                  f"{line[2]}\n"
                  f"-------------------------------------------------------\n")

            task_count += 1

    print("\nYou have viewed all tasks. Taking you back to the menu shortly...\n")


# == Function to view the tasks of the logged-in user ==
def view_mine():
    print("\nYour Task List:-\n")

    # Calling a function to refresh a dictionary (called: vm_task_info) which stores all task information. This ensures
    # the latest task information is being worked with.
    task_update()

    #   Looping through the vm_task_info dictionary and accessing the task information.
    for key in vm_task_info:
        # Usernames assigned to a task are stored in 'vm_task_info[key][0][0]'. This conditional check allows the
        # logged-in user to see their tasks.
        if vm_task_info[key][0][0] == current_username:
            print(vm_task_info[key][1])

    # Allowing the user to view a specific task or return to the main menu.
    while True:
        vm_user_input = int(input("Enter the task number to view a specific task or enter '-1' to return to the main "
                                  "menu: "))

        if vm_user_input == -1:
            print("\nTacking you back to the menu shortly...\n")
            break
        else:
            # Printing the string format of the task information.
            print(f"\n{vm_task_info[vm_user_input][1]}")

            # Allowing the user to make edits to a specific task or return to the main menu.
            vm_edit = input("Would you like to:\n"
                            "1. Mark the task as complete?\n"
                            "2. Edit who the task is assigned to?\n"
                            "3. Edit the due date?\n"
                            "4. I dont want to make any changes. Take me back to the main menu.\n"
                            "Please enter the corresponding number: ")

            # Return to main menu.
            if vm_edit == "4":
                print("\nTacking you back to the menu shortly...\n")
                break

            # Preventing a task from being edited if it has already been marked as complete.
            elif vm_task_info[vm_user_input][0][5] == "Yes":
                print("This task has been marked as complete. It cannot be edited. Taking you back to the previous "
                      "menu...")

            # Marking the task as complete.
            elif vm_edit == "1":
                with open('tasks.txt', 'r') as task_file:
                    vm_task_file = task_file.readlines()

                # Editing the list inside the task dictionary; this is where the task status is stored.
                vm_task_info[vm_user_input][0][5] = "Yes"

                vm_task_file[vm_user_input - 1] = ", ".join(vm_task_info[vm_user_input][0]) + "\n"

                with open('tasks.txt', 'w') as task_file:
                    task_file.writelines(vm_task_file)

                print("\nTask successfully edited.\n")

            # Editing who the task is assigned to.
            elif vm_edit == "2":
                with open('tasks.txt', 'r') as task_file:
                    vm_task_file = task_file.readlines()

                # Editing the list inside the task dictionary; this is where the username is stored.
                vm_task_info[vm_user_input][0][0] = input("Please enter the new username: ")
                vm_task_file[vm_user_input - 1] = ", ".join(vm_task_info[vm_user_input][0]) + "\n"

                with open('tasks.txt', 'w') as task_file:
                    task_file.writelines(vm_task_file)

                print("\nTask successfully edited.\n")

            # Editing the due date.
            elif vm_edit == "3":
                # Storing the text file in a variable.
                with open('tasks.txt', 'r') as task_file:
                    vm_task_file = task_file.readlines()

                # Editing the list inside the task dictionary; this is where the due date is stored.
                vm_task_info[vm_user_input][0][4] = input("Please enter the new due date (DD Mmm YYYY): ")

                vm_task_file[vm_user_input - 1] = ", ".join(vm_task_info[vm_user_input][0]) + "\n"

                with open('tasks.txt', 'w') as task_file:
                    task_file.writelines(vm_task_file)

                print("\nTask successfully edited.\n")


# == Function for updating the dictionary which stores the user login credentials ==
def user_info_update():
    with open('user.txt', 'r') as user_file:
        for line in user_file:
            # Processing the line to make it easier to work with.
            line = line.strip()
            username_stored, password_stored = line.split(", ")

            user_info[username_stored] = password_stored


# == Function for updating the dictionary which stores the task information ==
def task_update():
    with open('tasks.txt', 'r') as task_file:

        # Initialising the counter at '1' so that the task dictionary is 'one'-indexed.
        task_count = 1

        for line in task_file:

            # Processing the line to make it easier to work with.
            line = line.strip()
            line = line.split(", ")

            task_output = (f"\033[1mTASK #{task_count}\033[0m\n"
                           f"Task: {line[1]}\n"
                           f"Assigned to: {line[0]}\n"
                           f"Date assigned: {line[3]}\n"
                           f"Due date: {line[4]}\n"
                           f"Task complete?: {line[5]}\n"
                           f"Description:\n"
                           f"{line[2]}\n"
                           f"-------------------------------------------------------\n")

            # The dictionary stores tuples of the task information in 2 different formats: list and string.
            vm_task_info[task_count] = (line, task_output)
            task_count += 1


# == Function which generates a summary of the task completion statistics ==
def task_overview():
    task_update()

    with open('task_overview.txt', 'w') as task_overview_file:

        # Resetting the counters.
        task_count = 0
        uncompleted_overdue_count = 0
        overdue_count = 0

        # Calculating the statistics and writing to the task text file.
        for key in vm_task_info:

            # Conditional check to see if a task is complete.
            if vm_task_info[key][0][5] == "Yes":
                task_count += 1

            # Creating date objects of the due date and current date.
            date_due_object = datetime.strptime(vm_task_info[key][0][4], "%d %b %Y")
            date_today_object = datetime.strptime(date.today().strftime("%d %b %Y"), "%d %b %Y")

            # Conditional check to see if a task is not complete and overdue.
            if vm_task_info[key][0][5] == "No" and date_today_object > date_due_object:
                uncompleted_overdue_count += 1

            # Conditional check to see if a task is overdue.
            if date_today_object > date_due_object:
                overdue_count += 1

        tasks_generated = len(vm_task_info)
        tasks_completed = task_count
        tasks_uncompleted = len(vm_task_info) - tasks_completed
        tasks_uncompleted_percentage = round((tasks_uncompleted / len(vm_task_info)) * 100, 2)
        tasks_overdue_percentage = round((overdue_count / len(vm_task_info)) * 100, 2)

        task_overview_file.write(f" === TASK OVERVIEW ===\n"
                                 f"Total tasks generated: {tasks_generated}\n"
                                 f"Total number of completed tasks: {tasks_completed}\n"
                                 f"Total number of uncompleted tasks: {tasks_uncompleted}\n"
                                 f"Total number of uncompleted and overdue tasks: {uncompleted_overdue_count}\n"
                                 f"Tasks incomplete (%): {tasks_uncompleted_percentage}\n"
                                 f"Tasks overdue (%): {tasks_overdue_percentage}\n"
                                 f"-------------------------------------------------------\n")


# Function which generates a summary of the user statistics ==
def user_overview():

    # Updating the task dictionary and resetting the username list.
    task_update()
    username_list.clear()

    # Opening the relevant files, calculating the statistics and writing to the user overview text file.
    tasks_generated = len(vm_task_info)

    with open('user.txt', 'r') as user_file:
        for line in user_file:
            # Processing the line to make it easier to work with.
            line = line.strip()
            line = line.split(", ")

            username_list.append(line[0])

    user_count = len(username_list)

    with open('user_overview.txt', 'a') as user_overview_file:
        user_overview_file.truncate(0)
        user_overview_file.write(f" === USER OVERVIEW ===\n"
                                 f"Total number of users registered: {user_count}\n"
                                 f"Total number of tasks: {tasks_generated}\n"
                                 f"-------------------------------------------------------\n")

    # Resetting the counters.
    task_count = 0
    tasks_uncompleted_count = 0
    uncompleted_overdue_count = 0
    overdue_count = 0

    # Calculating the task statistics for each username.
    for name in username_list:
        for key in vm_task_info:

            if name == vm_task_info[key][0][0]:
                task_count += 1

                date_due_object = datetime.strptime(vm_task_info[key][0][4], "%d %b %Y")
                date_today_object = datetime.strptime(date.today().strftime("%d %b %Y"), "%d %b %Y")

                if vm_task_info[key][0][5] == "No":
                    tasks_uncompleted_count += 1

                if vm_task_info[key][0][5] == "No" and date_today_object > date_due_object:
                    uncompleted_overdue_count += 1

                if date_today_object > date_due_object:
                    overdue_count += 1

            tasks_assigned = task_count
            tasks_assigned_percentage = round((tasks_assigned / len(vm_task_info)) * 100, 2)

            if tasks_assigned == 0:
                tasks_uncompleted_percentage = 0
                tasks_completed_percentage = 0
                tasks_uncompleted_overdue_percentage = 0

            elif tasks_assigned > 0:
                tasks_uncompleted_percentage = round((tasks_uncompleted_count / tasks_assigned) * 100, 2)
                tasks_completed_percentage = 100 - tasks_uncompleted_percentage
                tasks_uncompleted_overdue_percentage = round((uncompleted_overdue_count / tasks_assigned) * 100, 2)

        with open('user_overview.txt', 'a') as user_overview_file:
            user_overview_file.write(f" === USER: {name} ===\n"
                                     f"Total tasks assigned: {tasks_assigned}\n"
                                     f"Total tasks assigned (%): {tasks_assigned_percentage}\n"
                                     f"Tasks assigned - completed (%): {tasks_completed_percentage}\n"
                                     f"Tasks assigned - uncompleted (%): {tasks_uncompleted_percentage}\n"
                                     f"Tasks assigned - uncompleted and overdue (%): "
                                     f"{tasks_uncompleted_overdue_percentage}\n"
                                     f"-------------------------------------------------------\n")

        # Resetting the counters.
        task_count = 0
        tasks_uncompleted_count = 0
        uncompleted_overdue_count = 0
        overdue_count = 0


# === Initialising variables ===
user_info = {}
vm_task_info = {}
username_list = []

# === Login Section ===

# Reading the username and password file (user.txt) and storing them into separate lists.
user_info_update()

# Using a while loop to facilitate the login process. If a user is unsuccessful, they will be asked again.
while True:
    current_username = input("Please enter your username: ")
    password = input("Please enter your password: ")

    if current_username not in user_info:
        print("Sorry, that username is not recognised. Try again.")
        continue

    elif current_username in user_info and password != user_info[current_username]:
        print("Sorry, that password is not recognised. Try again.")
        continue

    elif current_username in user_info and password == user_info[current_username]:
        print("\nYou have successfully logged in.\n")
        break

# Presenting the menu to the user. If the admin is logged in, they will have access to a separate menu.
while True:
    if current_username == "admin":
        menu = input("Select one of the following options below:\n"
                     "r  - Register a user\n"
                     "a  - Add a task\n"
                     "va - View all tasks\n"
                     "vm - View my task\n"
                     "gr - Generate reports\n"
                     "ds - Display statistics\n"
                     "e  - Exit\n"
                     "\nEnter here: ").lower()

    else:
        menu = input("Select one of the following options below:\n"
                     "r  - Register a user\n"
                     "a  - Add a task\n"
                     "va - View all tasks\n"
                     "vm - View my task\n"
                     "e  - Exit\n"
                     "\nEnter here: ").lower()

    # === Register a new user section ===
    # In this section, only the admin has permission to add a new user. They will be written to the 'user.txt' file.
    if menu == 'r':
        reg_user()

    # === Add a new task section ===
    # This section allows the user to add a new task. It will be written to the 'task.txt' file.
    elif menu == 'a':
        add_task()

    # === View all task section ===
    # This section allows the user to view all tasks and their details.
    elif menu == 'va':
        view_all()

    # === View my task section ===
    # This section allows the user to view all of their own tasks and their details.
    elif menu == 'vm':
        view_mine()

    # === Generate reports section ===
    # This section generates user and task statistics; they are written to their respective text files.
    elif menu == 'gr' and current_username == "admin":
        task_overview()
        user_overview()
        print("\nYour reports have been generated - please view the 'user_overview' and 'task_overview' files.\n"
              "Now taking you back to the main menu.\n")

    # === Display statistics section ===
    # This section allows the admin to view the user and task statistics.
    elif menu == 'ds' and current_username == "admin":
        task_overview()
        user_overview()

        with open('task_overview.txt', 'r') as task_overview_file:
            print(task_overview_file.read())

        with open('user_overview.txt', 'r') as user_overview_file:
            print(user_overview_file.read())

    elif menu == 'e':
        print("\nYou have successfully exited the task manager. Goodbye!!!")
        exit()

    else:
        print("\nYour input is not recognised. Please Try again.\n")
