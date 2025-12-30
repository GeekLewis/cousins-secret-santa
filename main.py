from dataclasses import dataclass
import readchar

import re


@dataclass
class UserPrefs:
    email_output: bool = True
    notify_child: bool = True
    notify_parent: bool = True


class Cousin:
    def __init__(
            self, childs_name: str, parents_name: str, 
            childs_email: str | None = None, 
            age: int | None = None) -> None:
        self.childs_name = childs_name
        self.parents_name = parents_name
        self.childs_email = childs_email
        self.age = age
        self.gift_for : str | None = None


class Parents:
    def __init__(
            self, parents_name: str, parents_email: str | None = None) -> None:
        self.parents_name = parents_name
        self.parents_email = parents_email
        self.children : list[str] = []

    def add_child(self, child_name: str) -> None:
        self.children.append(child_name)


def get_name(who: str) -> str | None:
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
        print("(Leave blank to cancel)\n")
        name:str = str(input(f"\nEnter {who}'s Name: "))
        if not name:
            return None
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
            print("\n\n")
            if char == "y":
                return True
            elif char == "n":
                return False
            else:
                print("\n\nNeeds (Y)es or (N)o")


def get_email(who: str) -> str:
    '''
    Asks the user to enter an email address with format validation and 
    spelling confirmation.
    
    :param who: Description of whose email is being requested 
    (e.g., "Child", "Parent")
    :type who: str
    :return: E-mail address as a string
    :rtype: str
    '''
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
    '''
    Validates the format of an email address using a regular expression.
    It only checks for basic structure and does not guarantee deliverability.

    :param email: The email address to validate
    :type email: str
    :return: True if the email is valid, False otherwise
    :rtype: bool
    '''
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.fullmatch(pattern, email):
        return True
    else:
        return False


def get_cousin(prefs: UserPrefs, parents_name: str) -> Cousin | None:
    childs_name = get_name("Child")
    if not childs_name:
        return None
    if prefs.notify_child:
        childs_email = get_email("Child")
    else:
        childs_email = None
    new_cousin = Cousin(
        childs_name=childs_name,
        parents_name=parents_name,
        childs_email=childs_email,
        age=None
    )
    return new_cousin
    
    
def add_cousin(family: dict, prefs: UserPrefs, parents_name: str) -> dict:
    new_cousin = get_cousin(prefs, parents_name)
    if not new_cousin:
        return family
    family[new_cousin.childs_name] = new_cousin
    return family


def get_family(families: dict, prefs: UserPrefs) -> dict:
    while True:
        parents_name = get_name("Parent")
        if not parents_name:
            return families
        elif parents_name in families:
            print(f"\nFamily for {parents_name} already exists.\n")
            continue
        break
    if prefs.notify_parent:
        parents_email = get_email("Parent")
    else:
        parents_email = None
    new_parents = Parents(
        parents_name=parents_name,
        parents_email=parents_email
    )
    families[parents_name] = new_parents
    return families


def main():
    print("Hello from cousins-secret-santa!")
    user_prefs = UserPrefs()
    families = {}
    cousins = {}
    
    

if __name__ == "__main__":
    main()