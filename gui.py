import functions
import PySimpleGUI



label = PySimpleGUI.Text("Type in a todo:")
input_box = PySimpleGUI.InputText(tooltip="Enter todo",key="todo")
add_button = PySimpleGUI.Button("Add")
edit_button = PySimpleGUI.Button("Edit")
complete_button = PySimpleGUI.Button("Complete")
exit_button = PySimpleGUI.Button("Exit")


window = PySimpleGUI.Window('My todo app',
                            layout=[[label], [input_box,add_button]],
                            font=('Helvetica',16))
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case PySimpleGUI.WIN_CLOSED:
            break


window.close()