

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
print(family)
print(family.__len__())
family.remove('Ahmet Salih')  #removes only one item from the list, list reorders automatically
print(family[3])

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
# friends_abroad = friends.copy()  # BE CAREFUL!! This modified both the copied and the non-copied list, because when we did .copy() we only copied the outermost list, and not the inner lists. Those lists still are the same list so changing one changes the other.
#
# print(friends_abroad[1][0])  # Bob
# friends_abroad[1][0] = "Jen"
#
# print(friends_abroad[1][0])  # Jen
# print(friends[1][0])  # Jen