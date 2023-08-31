import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    print(todo)
    todos.append(todo)
    functions.write_todos(todos)


st.title("My Todo App")
st.subheader("This tool allows you to track to-do tasks")
st.write("You can Add, Edit, and Complete tasks on the list")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="Enter a todo:", label_visibility="hidden",
              placeholder="Add a new todo...", on_change=add_todo,
              key="new_todo")