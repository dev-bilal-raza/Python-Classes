isAdmin = False

# if isAdmin:
#     print("Admin is here")



# if isAdmin:
#     print("Admin is here")
# print("Admin 1 is here")
   
 
# if "bilal" in std_list:
#     ...

# if "Hassan" in std_list:
#     print("You have an account")
# else:
#     print("You don't have an account")

# if "Hassan" in std_list:
#     print("You have an account")
# elif "Hacker" not in std_list :
#     print("Your db has secure")


# Ternory Operator
# print("You have an account" if "Hassan" in std_list else "Hassan is not in db")
std_list = ["bilal", "huzair", "fawad"]

message = "You have an account" if "Hassan" in std_list else "Hacker is not in db" if "Hacker" not in std_list else "You need to secure your db"

print("Message: ", message)

# Loop in Python

# for i in std_list:
#     print(i, end="\n") # default syntax

# for i in std_list:
#     print(i, end=" ")
    
# for i in std_list:
#     print(i)
# print("after loop: ", i)
# user_name = input("Please enter your name: ")

# print("bilal" == user_name)

# for i in std_list2:
#     # print(user_name)
#     if i ==  str(user_name):
#         print("You have successfully logged in")
#         break
# else:
#     print("Invalid name")

# admin_list = ["bilal", "hussain", "shami", "hamza"]
# std_list3 = ["huzair", "fawad", "hamza", "shami", "hamza"]

# extracted_list = []

# for i in admin_list:
#     for y in std_list3:
#         if (y == i):
#             if (y in extracted_list):
#                 print(f"{str(y).capitalize()} is already exist as an admin")
#             else:
#                 extracted_list.append(y)
#                 print(f"{y} is an admin")
            
print(list(char for char in "bilal")) 

    