"""Small reusable input helpers."""


def read_non_empty(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field cannot be empty. Please try again.")


def read_int(prompt, minimum=None, maximum=None):
    while True:
        try:
            value = int(input(prompt).strip())
            if minimum is not None and value < minimum:
                raise ValueError
            if maximum is not None and value > maximum:
                raise ValueError
            return value
        except ValueError:
            if minimum is not None and maximum is not None:
                print(f"Enter a whole number from {minimum} to {maximum}.")
            else:
                print("Enter a valid whole number.")


def confirm(prompt):
    while True:
        answer = input(prompt).strip().lower()
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("Please enter y or n.")
