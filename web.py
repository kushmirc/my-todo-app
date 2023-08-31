import streamlit as st
import functions

todos = functions.get_todos()
#st.set_page_config(layout="wide")

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    print(todo)
    todos.append(todo)
    functions.write_todos(todos)


st.title("My Todo App")
st.subheader("This tool allows you to track to-do tasks")
st.write("You can Add, Edit, and Complete <b>tasks<b> on the list",
         unsafe_allow_html=True)

st.text_input(label="Enter a todo:", label_visibility="hidden",
              placeholder="Add a new todo...", on_change=add_todo,
              key="new_todo")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

