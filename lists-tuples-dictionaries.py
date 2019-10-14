# dictionary_1 = {"isim" : "name", "soyisim" : "last name"}
# print(dictionary_1)
#
# for key in dictionary_1:
#     print(f"key is {key}, value is {dictionary_1[key]}")
#
# dictionary_2 = {"cep telefonu" : "mobile phone", "is adresi" : "work address"}
#
# print(dictionary_2)
#
# for key in dictionary_2:
#     dictionary_1[key] = dictionary_2[key]
# else:
#     print(dictionary_1)
#
#
# print(f"Isim translates to {dictionary_1['isim']}") #formatted string, key must be put in single quotes if the print quote is double quote.
#
# print(f'Isim translates to {dictionary_1["isim"]}') #formatted string, key must be put in double quotes if the print quote is single quote.
#
#
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
# for key, value in mydict.items():
  # print(f'Key: {key} Value: {value}')
for key in mydict.keys():
  print(f'Key: {key}, Value: {mydict[key]}')
print(type(mydict.values()))

print('\n\n')
# myfamily = {
#   "child1": {
#     "name": "Emil",
#     "year": 2004
#   },
#   "child2": {
#     "name": "Tobias",
#     "year": 2007
#   },
#   "child3": {
#     "name": "Linus",
#     "year": 2011
#   }
# }
#
# for obj, inner_dictionary in myfamily.items():
#     print(f"Name: {inner_dictionary['name']} Year: {inner_dictionary['year']}")

age = 36
year = 2019
txt = "My name is John, and I am {} in {}"
print(txt.format(age, year))

this_tuple = ('apple', 'kiwi', 'banana')
this_string = 'apple'
this_single_item_tuple = ('apple',) #IMPORTANT! if you don't put a comma to the end of a single tuple, then this will be interpreted as string!
this_list = ['apple', 'banana']
this_dictionary = {'name': 'tugba', 'last_name': 'alparslan'}
print(this_tuple, type(this_tuple), type(this_single_item_tuple),
      type(this_string), type(this_list), type(this_dictionary))

print('\n\n')

tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(type(tuple3[1]), type(tuple3[3]))
print(type(tuple3))
print('\n\n')


thisset = {'kiwi', 'apple', 'kiwi'}

for x in thisset:
  print(x, '**')



thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(thisdict)



print("Converting python range() to list")
even_list = list(range(2,10,2))
print("printing the even list", even_list)
odd_list = list(range(1,10,2))
print("Printing the odd list:", odd_list)



# my_dic_list = [{"name": "Elly", "age": 30}, {"name": "Ralph", "age": 50}]
# for x in my_dic_list:
#     print(x)

student_attendance = {"Elly": 90, "Ralph": 100}

for tuple_item in student_attendance.items():  # .items() function returns tuple list of dictionary ('Elly', 90)
    print("tuple_item:", tuple_item)

for key, value in student_attendance.items():  # assign tuple items to key, value pair
    print(f"key:{key}, value: {value}")

for key in student_attendance:
    print(f"key is: {key}")