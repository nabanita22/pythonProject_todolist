FILEPATH = "todo.txt"


def get_todos(filepath=FILEPATH):
    '''
    reads the todo text file in read mode and contains
    all the values in todos_local list
    '''
    with open(filepath, "r") as file:
        todos_local = file.readlines()
    return todos_local


def write_todos(todo_arg, filepath=FILEPATH):
    with open(filepath, "w") as file:
        file.writelines(todo_arg)
