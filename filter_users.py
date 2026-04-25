import json


def load_users():
    with open("users.json", "r") as file:
        return json.load(file)


def filter_users_by_name(name):
    users = load_users()
    filtered_users = [
        user for user in users
        if user.get("name", "").lower() == name.lower()
    ]

    for user in filtered_users:
        print(user)


def filter_users_by_age(age):
    users = load_users()
    filtered_users = [
        user for user in users
        if user.get("age") == age
    ]

    for user in filtered_users:
        print(user)


if __name__ == "__main__":
    filter_option = input(
        "Filter by 'name' or 'age': "
    ).strip().lower()

    if filter_option == "name":
        name_to_search = input("Enter name: ").strip()
        filter_users_by_name(name_to_search)

    elif filter_option == "age":
        try:
            age_to_search = int(input("Enter age: ").strip())
            filter_users_by_age(age_to_search)
        except ValueError:
            print("Age must be a valid number.")

    else:
        print("Filtering by that option is not supported.")