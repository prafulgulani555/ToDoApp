import streamlit as st
from streamlit import checkbox
import functions

todos = functions.get_todos()

def add_todos():
    todo_local = st.session_state["new_todo"] + "\n"
    todos.append(todo_local)
    functions.write_todos(todos)

    st.session_state["new_todo"] = ""

st.title("Todo app")

st.text_input(label="", placeholder="Add new todo....",
              on_change=add_todos, key="new_todo")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key = f"todo_{index}")
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[f"todo_{index}"]
        st.rerun()


