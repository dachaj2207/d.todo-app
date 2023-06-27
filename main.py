#from functions import get_todos,write_todos - Ovo sluzi kad hoces da pozoves samo odreddjene funkcije iz drugog fajla

import time
import functions
cur_time = time.strftime("Current date is: %D - and current time is %H Hours %M Minutes %S Seconds")
print(cur_time)
user_prompt = "Type add or show or edit or exit or complete:"

todos = []

while True:

    user_action = input(user_prompt)

    if user_action.startswith("add"):
        todo = user_action[4:] #4: sluzi da prekoci prva cetiri slova.Moze da se stavi i 4:8 to znaci da hvara samo uzmedju 4 i 6

        todos = functions.get_todos()

        todos.append(todo + "\n")

        functions.write_todos(todos)



    elif user_action.startswith("show"):
        # with iznad radi istu stvar kao i 3 linije koda ispod
        file = open("todos.txt", "r")
        todos = file.readlines()
        file.close()

        for index, item in enumerate(todos):
            item = item.strip("\n")
            item = item.capitalize()
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = functions.get_todos()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + "\n"

            functions.write_todos(todos)
        except ValueError:
            print("Your command is not valid.")
            continue # Vraca na pocetak loop-a, odnosno nastavlja da vrti loop
    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            todos = functions.get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)

            functions.write_todos(todos)

            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)
        except IndexError:
            print("Your command is not valid.")
        except ValueError:
            print("Please enter a valid number")
            continue
    elif user_action.startswith("exit"):
        break
    else:
        print("PLease use valid command")

print("Bye")







