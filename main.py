from dataclasses import dataclass
import readchar

import re


@dataclass
class UserPrefs:
    email_output: bool = True
    notify_chiild: bool = True
    notify_parent: bool = True


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


def add_cousin(prefs: UserPrefs) -> Cousin:
    childs_name = get_name("Child")
    if UserPrefs
    pass


def main():
    print("Hello from cousins-secret-santa!")
    user_prefs = UserPrefs()
    family = {}
    print(family)


if __name__ == "__main__":
    main()