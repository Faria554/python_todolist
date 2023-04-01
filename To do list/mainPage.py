import todolist

first_question = "What would you like to do?\n"
second_question = "What else do you wanto to do?\n"
print(first_question)

def main():
    actions = ['Add a new task', 'Read all the tasks', 'Remove a task', 'Clear list \n']
    for i, task in enumerate(actions):
        print(f"{i+1}. {task.strip()}")
    
    choice = int(input("Enter your choice (1-4): "))

    match choice:
        case 1:
            add = todolist.addtask()
            print(second_question)
            main()
        case 2:
            print("Here is your to do list: \n")
            read = todolist.readtask()
            print("\n", second_question)
            main()
        case 3:
            remove = todolist.deleteTask()
            print("\n", second_question)
            main()
        case 4:
            clear = todolist.clear_file("tasks.txt")  
            print(second_question)
            main()
  
if __name__ == "__main__":
    main()
