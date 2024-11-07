from typing import Callable, Any

def my_func(x):
    print("Hello World")
    
func = lambda x: print(x)
func(3)

users = ["hamza", "bilal", "huzair", "fawad"]

# login = lambda user: print("Welcome", user) if user in users else print("Invalid user")
# login("hamza")
def getuser(x, y):
    return x

# Callable[[parameterstype], returntype]

myfunc: Callable[[str, int], str] = getuser

# def login(user):
#     if user in users:
#         return user
#     else:
#         return [None, user][1] 


login: Callable[[str], str | None] = lambda user: user if user in users else [print("Invalid user"), user][1]
user = login("fawad1")
print(user)

# filter method
filter(lambda x)