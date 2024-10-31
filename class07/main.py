# Error Handling:

# try: it is for trying some functionality
# except: if functionality has not completed successfully
# else: If except has not got any error
# finally: it will run always
def error_handling():
    """
    arg: value
    This function returns a value in bool
    returType: 
    """
    try:
        # my_num = 1/0
        my_list = [1, 2, 3]
        print(my_list[4])
        print("Good Morning")
    except IndexError as bilal:
        print("Invalid Number", bilal)
    except ZeroDivisionError as err:
        print("Division Error: ", err)
    except Exception as err:
        print("Error while funtioning: ", err)
    else:
        print("Error has not catched.")
    finally:
        print("Thanks for checking!")

# error_handling()

# def login():
#     """
#     arg: value
#     This function returns a value in bool
#     returType: 
#     """
#     try:
#         user_list = ["hamza", "bilal", "huzair", "fawad"]
#         user_name = input("Enter your user name: ")
#         # while(not user_name):
#         #     user_name = input("Enter your user name: ")

#         if (not user_name):
#             print("Please enter a user name.")
#             return login()
#         elif (user_name not in user_list):
#             raise Exception("User name doesn't exist.")
#         print("Good Morning")
#     except IndexError as bilal:
#         print("Invalid Number", bilal)
#     except ZeroDivisionError as err:
#         print("Division Error: ", err)
#     except Exception as err:
#         print("Error while funtioning: ", err)
#     else:
#         print("Error has not catched.")
#     finally:
#         print("Thanks for checking!")

# # login.__doc__
# login()


### Classes

class Auth:
    db_connection = "postgres://bilal:123,aws.org"
    user_lists = ["bilal", "hamza", "fawad"]
    
    def __init__(self) -> None:
        pass
    
    def signup(self, user_name: str):
        self.user_lists.append(user_name)
        print("You have successfully signed up")
        
    def getUsers(self):
        print(self.user_lists)

my_auth = Auth()
my_auth.signup("bilal")    
my_auth.getUsers()