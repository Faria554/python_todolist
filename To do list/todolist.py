
#Function that allows the user to enter a new task
def addtask():
    task = input("Enter a new task: ") 
    with open("Working with files/To do list/tasks.txt", "a") as file:
            file.write(task + "\n")
    while True:
        task = input("Enter another task: ")
        if task == 'done':
            break 
        else:
            with open("Working with files/To do list/tasks.txt", "a") as file:
                file.write(task + "\n")
        

#Function that allows the user to read the tasks
def readtask():
    with open("Working with files/To do list/tasks.txt", "r") as file:
        # Use enumerate() to iterate over the lines of the file
        for i, line in enumerate(file):
            print(f"{i+1}. {line.strip()}")

#Function that allows the user to remove a task
def deleteTask():
    with open("Working with files/To do list/tasks.txt", "r") as file:
        lines = file.readlines()
        try:
            #Remove the line you want to delete
            deleteline = int(input("Which task do you want to delete: "))
            del lines[deleteline - 1]
        except:
            print("Error deleting the task")

    #Write the updated contents back to the file
    with open("Working with files/To do list/tasks.txt", "w") as file:
        file.writelines(lines)

    print("Here is your updated list: \n")
    #Reopen the file to print the updated contents with counts
    with open("Working with files/To do list/tasks.txt", "r") as file:
        # Use enumerate() to iterate over the lines of the file
        for i, line in enumerate(file):
            # Print the line with its count
            print(f"{i+1}. {line.strip()}")

# Function to Clear all the File
def clear_file(filename):
    # Clear the contents of the file with the given filename
    with open("Working with files/To do list/tasks.txt", "w") as file:
        file.truncate(0)
        print("All tasks have been deleted")



