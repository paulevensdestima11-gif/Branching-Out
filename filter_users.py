import json


def load_users():
    """Load users from JSON file."""
    with open("users.json", "r") as file:
        return json.load(file)


def filter_users(key, value):
    """Generic filter function for users."""
    users = load_users()

    filtered_users = [
        user for user in users
        if str(user.get(key, "")).lower() == str(value).lower()
    ]

    for user in filtered_users:
        print(user)


def get_age_input():
    """Safely get age input from user."""
    try:
        return int(input("Enter age: ").strip())
    except ValueError:
        print("Age must be a number.")
        return None


if __name__ == "__main__":
    option = input(
        "Filter by 'name', 'age', or 'email': "
    ).strip().lower()

    if option == "name":
        value = input("Enter name: ").strip()
        filter_users("name", value)

    elif option == "age":
        value = get_age_input()
        if value is not None:
            filter_users("age", value)

    elif option == "email":
        value = input("Enter email: ").strip()
        filter_users("email", value)

    else:
        print("Filtering by that option is not supported.")