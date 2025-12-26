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

def main():
    print("Hello from cousins-secret-santa!")


if __name__ == "__main__":
    main()
