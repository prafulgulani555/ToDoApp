import FreeSimpleGUI as sg
import functions

label = sg.Text("Enter a ToDo")
input_box = sg.InputText(tooltip = "Enter ToDo", key = "todo")
add_button = sg.Button("Add")

list_box = sg.Listbox(values = functions.get_todos(), key = 'todos',
                      enable_events = True, size = (45, 10))
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window('ToDo App',
                   layout = [[label],
                             [input_box, add_button],
                             [list_box, edit_button, complete_button],
                             [exit_button]],
                   font = ('Helvetica', 20))

while True:
    event, values = window.read()
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values = todos)
            window['todo'].update(value = '')

        case "Edit":
            edit_todo = values['todos'][0]
            new_todo = values['todo']

            todos = functions.get_todos()
            index = todos.index(edit_todo)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos'].update(values = todos)
            window['todo'].update(value = '')

        case "todos":
            window['todo'].update(value = values['todos'][0])

        case "Complete":
            complete_todo = values['todos'][0]
            todos = functions.get_todos()
            todos.remove(complete_todo)
            functions.write_todos(todos)
            window['todos'].update(values = todos)
            window['todo'].update(value = '')

        case "Exit":
            break

        case sg.WINDOW_CLOSED:
            break

window.close()