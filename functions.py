FILEPATH = "todos.txt"

def get_todos(): # Ovako se prave funkcije
    """ Sa ovom funkcijom citamo linije iz text fajla"""
    with open(FILEPATH, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local # Cela ova funkcija vraca samo sto je u returnu


def write_todos(todos):
    """Sa ovom funkcijom pisemo komande u txt file"""
    with open(FILEPATH, "w") as file:
        file.writelines(todos)


if __name__ == "__main__": # Ovo sluzi da ti ne prebaci ovaj print u fajl koji si pozvao ovaj.
    print("Hello from functions")