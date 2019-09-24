# def new_function(country="Turkey"):  #DEFAULT PARAMETER AND RETURN VALUE
#
#     print(f'I am from {country}')
#
#     if country != 'Turkey':
#         return True
#     else:
#         return False
#
#
# user_country = input('Please enter where you are from')
# print(len(user_country))
# if (new_function(user_country)):
#     print("So, you are not Turkish")
# else:
#     print('You are Turkish')



# def pass_a_list(list_of_args):      #PASSING A LIST AS ARGUMENT
#     for x in list_of_args:
#         print(x)
#
# mylist = ["Esma", "Tugba", "Fatma"]
# pass_a_list(mylist)





mylist = ["Esma", "Tugba", "Fatma"]
def pass_unknown_num_of_args(*arg_list):        #PASSING UNKNOWN NUMBER OF ARGUMENTS
    for x in arg_list:
        print(x)


pass_unknown_num_of_args("Glenn", "Arnold", "Ashley", "Greg", "Linda") #Will pass as multiple arguments
pass_unknown_num_of_args(mylist)    #will pass as a single argument, the function will print ['Esma', 'Tugba', 'Fatma']. Instead should call like this: pass_unknown_num_of_args("Esma", "Tugba", "Fatma")
pass_unknown_num_of_args(*mylist)    #will pass as an argument list, the function will print 'Esma', 'Tugba', 'Fatma'.


# def tri_recursion(k):
#   if(k>0):
#     result = k+tri_recursion(k-1)
#     print(result)
#   else:
#     result = 0
#   return result
#
# print("\n\nRecursion Example Results")
# tri_recursion(6)