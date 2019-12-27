# Python program to illustrate
# https://www.geeksforgeeks.org/args-kwargs-python/

# **kwargs is used for keyword-value paired arguments
def pass_kwargs1(**kwargs):
    for key, value in kwargs.items():
        print("%s = %s *" % (key, value))

    # Driver code


pass_kwargs1(first='This', mid='is', last='Python')


# Python program to illustrate  **kargs for
# variable number of keyword arguments with
# one extra argument.

def pass_kwargs2(arg1, **kwargs):
    for key, value in kwargs.items():
        print("%s : %s" % (key, value))

    # Driver code


pass_kwargs2("Hi", First='I', Mid='learn', Last='Python')


def pass_kwargs3(**kwargs):
    for key, value in kwargs.items():
        print("Name: %s Lastname: %s " % (key, value))

name_lastname = {"Nick": "Stevenson", "Elsa": "Frederick"}
# when it's a key-value pair,to send separate arguments you put 2 asterisk before the variable
pass_kwargs3(**name_lastname)


#Using *args and **kwargs to call a function

def arguments_here(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)


# Now we can use *args or **kwargs to
# pass arguments to this function :
my_args = ("I", "love", "Python")
arguments_here(*my_args)

my_kwargs = {"arg2": "LOVE", "arg1": "I", "arg3": "PYTHON"}
arguments_here(**my_kwargs)


def pass_unknown_num_of_args(*arg_list):  # PASSING UNKNOWN NUMBER OF ARGUMENTS
    for x in arg_list:
        print(x)


my_list = ["Ray", "Eva", "Rose"]

pass_unknown_num_of_args("Glenn", "Arnold", "Ashley", "Greg", "Linda")  # Will pass as multiple arguments
print("After passing as a single argument list (my_list) :")
pass_unknown_num_of_args(my_list)  # Will pass as a single argument, the function will only print ["Ray", "Eva", "Rose"]
print("After passing as multiple argument list (*my_list) :")
pass_unknown_num_of_args(*my_list)    # will pass as an argument list, the function will print "Ray", "Eva", "Rose"