# Python program to illustrate
# *kwargs for variable number of keyword arguments
# https://www.geeksforgeeks.org/args-kwargs-python/


def pass_args1(**kwargs):
    for key, value in kwargs.items():
        print("%s = %s *" % (key, value))

    # Driver code


pass_args1(first='This', mid='is', last='Python')


# Python program to illustrate  **kargs for
# variable number of keyword arguments with
# one extra argument.

def pass_args2(arg1, **kwargs):
    for key, value in kwargs.items():
        print("%s : %s" % (key, value))

    # Driver code


pass_args2("Hi", First='I', Mid='learn', Last='Python')


#Using *args and **kwargs to call a function

def arguments_here(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)


# Now we can use *args or **kwargs to
# pass arguments to this function :
my_args = ("I", "love", "Python")
arguments_here(*my_args)

my_kwargs = {"arg1": "I", "arg2": "LOVE", "arg3": "PYTHON"}
arguments_here(**my_kwargs)



my_list = ["Ray", "Eva", "Rose"]


def pass_unknown_num_of_args(*arg_list):  # PASSING UNKNOWN NUMBER OF ARGUMENTS
    for x in arg_list:
        print(x)


pass_unknown_num_of_args("Glenn", "Arnold", "Ashley", "Greg", "Linda")  # Will pass as multiple arguments
print("After passing as a single argument list: (my_list)")
pass_unknown_num_of_args(my_list)  # Will pass as a single argument, the function will only print ["Ray", "Eva", "Rose"]
print("After passing as multiple argument list: (*my_list)")
pass_unknown_num_of_args(*my_list)    # will pass as an argument list, the function will print "Ray", "Eva", "Rose"