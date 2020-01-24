# Python program to illustrate
# https://www.geeksforgeeks.org/args-kwargs-python/


# **kwargs is used for keyword-value paired arguments
def pass_kwargs1(**kwargs):
    for key, value in kwargs.items():
        print("%s = %s" % (key, value))

    # Driver code


pass_kwargs1(first='This', mid='is', last='Python')

print("")

# Python program to illustrate  **kwargs for
# variable number of keyword arguments with
# one extra argument.


def pass_kwargs2(arg1, **kwargs):
    for key, value in kwargs.items():
        print("%s : %s" % (key, value))

    # Driver code


pass_kwargs2("Hi", First='I', Mid='learn', Last='Python')

print("")


def pass_kwargs3(kwargs):
    for key, value in kwargs.items():
        print("Name: %s, Last Name: %s " % (key, value))


full_name = {"Nick": "Stevenson", "Elsa": "Frederick"}
# when it's a key-value pair,to send as separate arguments you put 2 asterisk before the variable
pass_kwargs3(full_name)

print("")


# Using *args and **kwargs to call a function
def arguments_here(name, last_name, age):
    print("Name:", name)
    print("Last Name:", last_name)
    print("Age:", age)


# Now we can use *args or **kwargs to
# pass arguments to this function :
my_args = ("Tugba", "Alparslan", "36")
print("\nPrinting *args:")
arguments_here(*my_args)


print("\nPrinting **kwargs:")
my_kwargs = {"last_name": "ALPARSLAN", "name": "TUGBA", "age": "36"}  # function's argument names must match the dictionary's key values
arguments_here(**my_kwargs)


def pass_args(*arg_list):  # PASSING UNKNOWN NUMBER OF ARGUMENTS
    for x in arg_list:
        print(x)


my_list = ["Ray", "Eva", "Rose"]
name_dictionary = {"name1": "Ray", "name2": "Eva", "name3": "Rose"}

print("\nAfter passing as multiple arguments--> pass_args(\"Ray\", \"Eva\", \"Rose\"):")
pass_args("Ray", "Eva", "Rose")  # Will pass as multiple arguments
print("\nAfter passing as a list--> pass_args(my_list) :")
pass_args(my_list)  # Will pass as a single argument, the function will only print ["Ray", "Eva", "Rose"]
print("\nAfter passing as extracted args --> pass_args(*my_list) :")
pass_args(*my_list)    # will pass unpacked my_list - as an argument list, the function will print "Ray", "Eva", "Rose"

