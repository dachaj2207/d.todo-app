import functions
import PySimpleGUI

label = PySimpleGUI.Text("Type in a todo:")
input_box = PySimpleGUI.InputText(tooltip="Enter todo")
add_button = PySimpleGUI.Button("Add")
edit_button = PySimpleGUI.Button("Edit")
complete_button = PySimpleGUI.Button("Complete")
exit_button = PySimpleGUI.Button("Exit")


window = PySimpleGUI.Window('My todo app', layout=[[label], [input_box,add_button]])
window.read()
window.close()