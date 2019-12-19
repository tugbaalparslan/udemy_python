#  BELOW ARE EXAMPLES OF LIST COMPREHENSION AND LAMBDA FUNCTIONS

print((lambda x, y: x+y)(5, 7))  # One way to write LAMBDA function

sum_func = lambda x, y: x+y  # Another way to write LAMBDA function
print(sum_func(5, 8))

list_a = [1, 2, 3, 4]
list_b = []


list_b = [x*2 for x in list_a]  # LIST COMPREHENSION
print(f"List B is: {list_b}")


def double_list(num):
    return 2 * num


list_c = [double_list(x) for x in list_a]
print(f"List C is: {list_c}")

# BELOW ARE EXAMPLES OF DICTIONARY COMPREHENSION

users = [(0, "Bob", "passwd123"),
         (1, "Rebeca", "holy78tt"),
         (2, "Daniel", "danmo34er"),
         (3, "Jamie", "123er54")]

# now user_map is:                                  # manuel way to create the user_map - FOR INFO, ALWAYS COMMENTED OUT
# user_map = [
#          "Bob": (0, "Bob", "passwd123"),
#          "Rebeca": (1, "Rebeca", "holy78tt"),
#          "Daniel": (2, "Daniel", "danmo34er"),
#          "Jamie": (3, "Jamie", "123er54")
# ]

user_map = {item[1]: item for item in users}        # Creating the user_map using list comprehension
print(user_map)

# user_input_name = input("Please enter your user name:")
# user_input_password = input("Please enter your password:")

# if user_input_name in user_map.keys():  # Check if the entered user id exists in the dictionary list
#     _, uid, password = user_map[user_input_name]  # Ignoring the first item of the tuple using the underscore
#     if user_input_password == password:
#         print("Your details are correct !")
#     else:
#         print("Your details are incorrect!")
# else:
#     print("There is no such user in the system!")

#  BELOW IS AN EXAMPLE OF TRY-CATCH VERSION OF THE CODE ABOVE

try:  # Check if the entered user id exists in the dictionary list
    _, uid, password = user_map[user_input_name]  # Ignoring the first item of the tuple using the underscore
    if user_input_password == password:
        print("Your details are correct !")
    else:
        print("Your details are incorrect!")
except:
    print("There is no such user in the system!")


# BELOW IS EXAMPLE OF FILTER FUNCTION - filters a list according to a given set of rules to create a new list
# filter function returns a filter object. takes 2 parameters: (function to filter, list to filter)

def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False


all_nums = [1, 5, 11, 17, 18, 23, 26]

even_list = list(filter(is_even, all_nums))  # using the filter function with a standard function, then converting the resulted filter object to a list
ev_list = list(filter(lambda x: x % 2 == 0, all_nums))  # using the filter function with a lambda function
for x in ev_list:
    print("filter function using lambda function:", x)
for x in even_list:
    print("filter function using a standard function:", x)



