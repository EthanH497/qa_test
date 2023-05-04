from .services import (
    find_all_users,
    insert_one_user,
    update_one_user,
    delete_one_user
)


# Clears the database
def clear_db():
    users = find_all_users()

    for user in users:
        delete_one_user(user["client_code"], user["organization"])


# Test for the find_all_users service
def test_find_all():
    clear_db()  # Clears the database to ensure the test runs properly

    # Adds two users to the database
    user_a = {"client_code": "1234", "organization": "Test Organization"}
    insert_one_user(user_a["client_code"], user_a["organization"])
    user_b = {"client_code": "5678", "organization": "Test Organization"}
    insert_one_user(user_b["client_code"], user_b["organization"])

    # Retrieves list of users from the database
    users = find_all_users()
    count = 0

    # Counts the number of users retrieved
    for user in users:
        count += 1

    # If the number of users counted matches the length of the users object, the test is successful
    assert count == len(users)


def test_insert_one():
    clear_db()  # Clears the database to ensure the test runs properly

    # Inserts a user to the database and stores the id of the new user
    user_a = {"client_code": "1234", "organization": "Test Organization"}
    user_id = insert_one_user(user_a["client_code"], user_a["organization"])
    count = 0

    # Retrieves list of users from db
    users = find_all_users()

    # Checks the users list for the one with a matching id
    for user in users:
        if user_id == user["_id"]:
            count += 1

    # If the count is 1, the new user was found and the test is successful
    assert count == 1


def test_update_one():
    clear_db()  # Clears the database to ensure the test runs properly

    # Adds a user to the database
    user_a = {"client_code": "1234", "organization": "Test Organization"}
    insert_one_user(user_a["client_code"], user_a["organization"])

    # New code for the user
    new_code = "5678"

    # Replaces the users client code with the new code and stores the number of users modified
    updated = update_one_user(user_a["client_code"], new_code)

    # If the number of modifications made is 1, the test is successful
    assert updated == 1


def test_delete_one():
    clear_db()  # Clears the database to ensure the test runs properly

    # Adds a user to the database
    user_a = {"client_code": "1234", "organization": "Test Organization"}
    insert_one_user(user_a["client_code"], user_a["organization"])

    # Deletes the user and stores the number of users deleted
    deleted = delete_one_user(user_a["client_code"], user_a["organization"])

    # If the number of users deleted is 1, the test is successful
    assert deleted == 1
