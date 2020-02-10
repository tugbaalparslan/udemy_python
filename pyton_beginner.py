# Python program to demonstrate the use of join function to join list elements with a character.

list1 = ['1', '2', '3', '4']
s = "-"
s = s.join(list1) # joins elements of list1 by '-' and stores in string s - which is 1-2-3-4
print(s)


# age = input("Enter your age:")
# age_as_number = int(age)
# months = age_as_number*12
# months_as_string = str(months)
# print("your age in months is: ", months_as_string)
#
# print('Entered age multiplied with 2 is:', age_as_number*2)
# or you can write it as:  print('Entered age multiplied with 2 is:', int(age)*2)


# this is a multiline comment. write your comment then
# select the lines to comment out : command+front slash


# FSTRING EXAMPLE ********************************************
# this is an example of fstring -> formatted string)
# age = 30
# # print(f'Next year you will be {age+1}')
# #
# # age = input("what is your age?")
# # print(f'you are alive for {int(age)*360*24*60*60} seconds')



# LISTS ******************************************************    len, insert, append, remove, assign, copy, count lists
family = ['Esma','Tugba','Fatma']
print(family[2])
print(len(family))

family.insert(3, 'Ahmet Salih') #inserts object to the given index, only one item to the list. List reorders automatically
# family.append('Ahmet Salih') #appends only one item to the list , list reorders automatically
family.append('Hamza')
family.append('Nesrin')
print(family.__len__(), family)
family.remove('Ahmet Salih')  #removes only one item from the list, list reorders automatically
print(family)
family.pop()
print("After pop() function: ", family)

# LISTS INSIDE LISTS EXAMPLE *************************************
#  friends = [['Ayse', 29], ['Aysenur', 31], ['Aysegul', 17]]
# print(friends)
# friends.append(["Aisha", 3])
# print("After adding an extra to the list:" , friends)
# print(len(friends))
# print(friends[1][0])

# ASSIGNING AND COPYING LISTS

family_female = family  # pitfall!! family and family_female are now exactly the same lists. Any changes made to one list will affect the other. To avoid this, use copy function instead
family_female.remove('Hamza')
print("\n\n*** WRONG - DONE WITH ASSIGNED LISTS ***\n\nFemales in the family are: " + str(family_female) + '\n' + 'Family members are:' + str(family) )


family = ['Hamza', 'Nesrin', 'Esma', 'Tugba', 'Fatma']
# family.sort()
family_females = family.copy()
family_females.remove('Hamza')
print("\n\n*** CORRECT  - DONE WITH COPIED LISTS ***\n\nFemales in the family are: " + family_female.__str__() + '\n' + 'Family members are:' + str(family) + f'\nThere are {family.__len__()} people in this family')


# print(family.index('Nesrin'))
# friends = [
#     ["Rolf", 24],
#     ["Bob", 30],
#     ["Anne", 27]
# ]
#
# BE CAREFUL!! This modified both the copied and the non-copied list,
# because when we did .copy() we only copied the outermost list,
# and not the inner lists. Those lists still are the same list so changing one changes the other.
# friends_abroad = friends.copy()
#
# print(friends_abroad[1][0])  # Bob
# friends_abroad[1][0] = "Jen"
#
# print(friends_abroad[1][0])  # Jen
# print(friends[1][0])  # Jen


class User:
    class_name = "This is class variable, not bound by an object"

    def __init__(self, _id, name, passwd):
        self.id = _id
        self.name = name
        self.password = passwd


Users = [
    User(123, "Alison", "12abd"),
    User(124, "Raleigh", "33xyz")
    ]

new_dic = {u.id: u for u in Users}

print(User.class_name)


list_u = [2,4,6,8,10]

double_nums = [x*2 for x in list_u]
print(double_nums)


def nested_function(n):  # arguments passed to the outer function are all accessible from inner functions

    print("outer function", n)
    x, y = 3, 5

    def inner_function1():
        print("inner function1:", n, x, y)  # Inner functions can access outer functions variables but can't change them
        # x += 1  # you cannot change outer function's variable. they are all immutable
    x += 1  # below this line, x will be x + 1, inner_function2 will read the new value

    def inner_function2():
        print("inner function2:", n, x, y)

    inner_function1()  # In order to access the inner function, it needs to be called
    inner_function2()


nested_function(10)


a = 3
print(a<<2)