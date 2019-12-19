

def print_me(x):
    global a

    print('a is:', a)
    a = [2]

    print("now a is:", a)

    print("x is:", x)
    x.append(45)
    print("**x is:", x)

    a.append(6)
    print("**now a is:", a)
    a = [0]
    print("**now a is:", a)


a = [3]
print_me(a)
print("a in the local space is:", a)
print("\n\n")

# **************************


y = 5


def f1():
    y = 9  # local variable is defined, so x is considered as local
    print(y)


f1()
print(y)
# **************************


x = [1, 2, 3, 4, 5]


def f1():
    print(x)  # x is yet not defined, so it will use the global x
    x.append(6)  # if x = [5] (assignment) made here,will give err to tell we must define x as "global x" or "local x"


f1()
print(x)


# def f1(x):
#
#     print(id(x))
#     x = 5
#     print(id(x))
#     print(x)
#
# x = 3
# print(id(x))
#
# f1(x)
# print(x)
#
# str1 = "geek"
# print(id(str1))
#
# str2 = "geek"
# print(id(str2))
#
# print(id("geek"))
#
# # This will return True
# print(id(str1) == id(str2))

