

def printme(x):
    global a

    print('a is:', a)
    # a = [2]

    print("now a is:", a)

    print("x is:", x)
    x.append(45)

    a.append(6)
    a=[0]
    print("**now a is:", a)

    print("**x is:", x)

# a = [3]
# printme(a)
# print(a)

#**************************

# x = 5
#
#
# def f1():
#     x = 9  #local variable is defined, so x is considered as local
#     print(x)
#
# f1()
# print(x)

#**************************



# x = [1,2,3,4,5]
#
# def f1():
#     print(x)  #  x is not defined, so it will use the global x
#     x.append(6)  #  if we had wrote x = [5] (assignment) we would get an err to tell us we must define x either global x or local x
#
# f1()
# print(x)


#**************************



def f1(x):
    # print(id(x))

    x = 5
    print(id(x))
    print(x)

x = 3
print(id(x))

f1(x)
print(x)

str1 = "geek"
print(id(str1))

str2 = "geek"
print(id(str2))

print(id("geek"))

# This will return True
print(id(str1) == id(str2))

