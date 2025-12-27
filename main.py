import readchar


class Cousin:
    def __init__(
            self, kids_name: str, parents_name: str, 
            kids_email: str | None, parents_email: str | None, 
            age: int | None) -> None:
        self.kids_name = kids_name
        self.parents_name = parents_name
        self.kids_email = kids_email
        self.parents_email = parents_email
        self.age = age
        self.gift_for : str | None = None


def get_name(who: str) -> str:
    name: str = ""
    while True:
        name:str = str(input(f"\nEnter {who}'s Name: "))
        if not name:
            print("Name can't be empty.\n")
            continue
        elif check_spelling(f"{who}'s name", name) == True:
            return name
        else:
            print(' ')


def check_spelling(field: str, spelling: str) -> bool:
    while True:
            print(f"\nConfirm the {field} is {spelling}")
            print("Is this correct? (Y/N)", end='', flush=True)
            char = readchar.readchar().lower()
            if char == "y":
                return True
            elif char == "n":
                return False
            else:
                print("\n\nNeeds (Y)es or (N)o")


def add_cousin() -> object:
    pass


def main():
    print("Hello from cousins-secret-santa!")
    family = []
    print(family)
    kids_name = get_name("Child")
    print(f"\n{kids_name}")
    parents_name = get_name("Parent")
    print(f"\n{kids_name}'s parent is {parents_name}")


if __name__ == "__main__":
    main()