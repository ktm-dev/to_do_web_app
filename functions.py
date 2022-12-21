
FILEPATH = 'todos.txt'

def get_todos(file_path_local=FILEPATH):
    with open(file_path_local, 'r') as file_local:
        todos_local = file_local.readlines()
        return todos_local
def write_todos(todos_arg,file_path_local=FILEPATH):
    with open(file_path_local, 'w') as file:
        file.writelines(todos_arg)

#only executed if this file is run
if __name__ == '__main__':
    print(get_todos())