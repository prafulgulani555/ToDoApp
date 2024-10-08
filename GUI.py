import FreeSimpleGUI as sg
import functions
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

sg.theme("DarkPurple4")

clock = sg.Text("", key = "clock")
label = sg.Text("Enter a ToDo")
input_box = sg.InputText(tooltip = "Enter ToDo", key = "todo")
add_button = sg.Button("Add")

list_box = sg.Listbox(values = functions.get_todos(), key = 'todos',
                      enable_events = True, size = (45, 10))
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window('ToDo App',
                   layout = [[clock],
                             [label],
                             [input_box, add_button],
                             [list_box, edit_button, complete_button],
                             [exit_button]],
                   font = ('Helvetica', 10))

while True:
    event, values = window.read(timeout = 10)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values = todos)
            window['todo'].update(value = '')

        case "Edit":
            try:
                edit_todo = values['todos'][0]
                new_todo = values['todo']

                todos = functions.get_todos()
                index = todos.index(edit_todo)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values = todos)
                window['todo'].update(value = '')
            except IndexError:
                sg.popup("Please select an todo first.", font = ('Helvetica', 10))

        case "todos":
            window['todo'].update(value = values['todos'][0])

        case "Complete":
            try:
                complete_todo = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(complete_todo)
                functions.write_todos(todos)
                window['todos'].update(values = todos)
                window['todo'].update(value = '')
            except IndexError:
                sg.popup("Please select an todo first.", font = ('Helvetica', 10))

        case "Exit":
            break

        case sg.WINDOW_CLOSED:
            break

window.close()