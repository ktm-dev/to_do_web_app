import streamlit as st
import functions as f


todos = f.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    f.write_todos(todos)



st.title("My to do app")
st.subheader("This is a todo app")

for index,todo in enumerate(todos):

    checkbox = st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        f.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()




st.text_input(label="enter to do here:",placeholder="Add todo here",
              on_change=add_todo,key='new_todo')


# st.session_state