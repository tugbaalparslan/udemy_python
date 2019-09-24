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

