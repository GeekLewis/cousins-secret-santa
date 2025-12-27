import readchar
import re


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
    '''
    Prompts the user to enter a person's name with spelling confirmation.
    
    Repeatedly asks for input until a non-empty name is provided and
    the user confirms the spelling is correct.
    
    :param who: The role or relationship of the person (e.g., "Child", "Parent")
    :type who: str
    :return: The confirmed name entered by the user
    :rtype: str
    '''
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
    '''
    Asks the user to confirm if the entered text is spelled correctly.
    
    Displays the field name and value, then waits for a single Y/N keypress.
    Repeats the prompt if an invalid key is pressed.
    
    :param field: Description of what is being confirmed (e.g., "Child's name")
    :type field: str
    :param spelling: The text value to be confirmed
    :type spelling: str
    :return: True if user confirms (Y), False if user rejects (N)
    :rtype: bool
    '''
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


def get_email(who: str) -> str:
    email:str = ""
    while True:
        email = str(input(f"\nEnter {who}'s E-mail: "))
        if not email:
            print("E-mail can't be empty.\n")
            continue
        valid: bool = check_email_format(email)
        if not valid:
            print("E-mail format is not valid.\n")
            continue
        elif check_spelling(f"{who}'s e-mail", email) == True:
            return email
        else:
            print(' ')


def check_email_format(email: str) -> bool:
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.fullmatch(pattern, email):
        return True
    else:
        return False


def add_cousin() -> object:
    pass


def main():
    print("Hello from cousins-secret-santa!")
    family = []
    print(family)
    kids_name = get_name("Child")
    print(f"\n{kids_name}")
    kids_email = get_email("Child")
    print(f"\n{kids_name}'s email is {kids_email}")
    parents_name = get_name("Parent")
    print(f"\n{kids_name}'s parent is {parents_name}")
    parents_email = get_email("Parent")
    print(f"\n{parents_name}'s email is {parents_email}")


if __name__ == "__main__":
    main()