from typing import Callable

# Copy by value vs reference

# user_name = "Bilal"
# friend_name = user_name
# friend_name = "Mustafa"

# print(friend_name)
# print(user_name)


# list_1: list = []
# list_2: list = list_1

# print(list_1 is list_2)
# print(id(list_1))

student_lists = ["hamza", "bilal", "bushra", "raheela", "ahsaan"] 

# Functions
def login(users: list[str]) -> list[str] | None:
    valid_users: list[str] = [] 
    for user in users:
        if user.lower() in student_lists:
            valid_users.append(user)
            print(f"Correct User: {user}")
        else:
            print(f"Invalid User: {user}")
    return valid_users

valid_user = login(["Bilal", "Mustafa", "huzair"])
# we need to send an email if user exist in db
print("We have sent an email for these users: ", valid_user)


# Positional Parameters
# def cv_lower(user_name: str) -> str:
#     return user_name.lower()

# Default Parameters
# def cv_lower(user_name: str | None = "Bilal"):
#     print(user_name)

# cv_lower()

# Optional Parameters
# def cv_lower(user_name = None):
#     print(user_name)

# cv_lower()


# Rest Operators
# def cv_lower(user_name: str, *users):
#     print(user_name)
#     print(users)

# valid_users = ["Bilal", "Mustafa", "huzair"]
# cv_lower("bilal", "hamza", "huzair")

# Spread Operators
# def cv_lower(user_name: str, user1, user2, *user3):
#     print(user_name)
#     print(user1)
#     print(user3)

# valid_users = ["Bilal", "Mustafa", "huzair", "fawad"]
# cv_lower("bilal", *valid_users)

# def cv_lower(user_name: str):
#     return user_name.lower()

# def add_in_db(user_name: str):
#     lowered_user_name = cv_lower(user_name)
#     print(f"Add {lowered_user_name} in db")
    
# add_in_db("Bilal")

# Nested Functions
# def add_in_db(user_name: str):
#     def cv_lower(user_name):
#         return user_name.lower()
#     print(f"Add {cv_lower(user_name)} in db")
    
# add_in_db("Bilal")


def add_in_db(user_name: str, callback: Callable):
    if (user_name == "admin"):
        callback(1, user_name, "Your are an admin")
    else:
        callback(0, user_name,"You are a user")

def handler(status: int, user: str, message: str):
    if (status == 1):
        print(message)
        print(f"Valid user: {user}")
    elif status == 0:
        print(message)
        print(f"Invalid user: {user}")

add_in_db("Bilal", handler)