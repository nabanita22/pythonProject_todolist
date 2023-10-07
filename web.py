import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    new_todo = st.session_state["new_todo"] + "\n"
    todos.append(new_todo)
    functions.write_todos(todos)


st.title("My Todo App")
st.subheader("This is my todo app")
st.text("This app is to increase your productivity")

for do in todos :
    checkbox = st.checkbox(do, key=do)
    if checkbox:
        todos.remove(do)
        functions.write_todos(todos)
        del st.session_state[do]
        st.rerun()

st.text_input(label="", placeholder="Add new Todo...",
              on_change=add_todo,
              key="new_todo")
