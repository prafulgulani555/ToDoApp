import FreeSimpleGUI as sg
import functions

label = sg.Text("Type in a ToDo")
input_box = sg.InputText(tooltip = "Enter ToDo", key = "todo")
add_button = sg.Button("Add")

window = sg.Window('ToDo App',
                   layout = [[label], [input_box, add_button]],
                   font = ('Helvetica', 20))

while True:
    event, values = window.read()
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case sg.WINDOW_CLOSED:
            break

window.close()