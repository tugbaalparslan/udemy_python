# age = input('Please enter your age:')
#
# if not age:
#     print('You know you need to enter your age to see how I respond')
# else:
#     age = int(age)
#     #  COMPOUND STATEMENTS - chaining clauses together
#     if age < 17:
#         print('Oh very young, you are dancing on the earth for a short while!')
#
#     elif age >= 35:
#         print('Wise years')
#     else:
#         print('Dynamic years!')


# countries_visited =['Turkey', 'Germany', 'USA', 'France', 'Italy', 'Saudi Arabia', 'Maldives']
#
# country_input = input('Please enter a country name you visited so far:')
#
#
# if country_input.upper in countries_visited:
#     print('Well, I have been there')
# else:
#     print('Oh, I\'ve never been there before!')





#  this code aims to calculate the average of the grades
# grades = [90, 80, 78, 100, 96, 80, 60]
#
# total = 0
# for grade in grades:  # OR ALTERNATIVELY :)) ---> total = sum(grades)
#     total += grade
#
# avg_grade = total / len(grades)
#
# print(f"Your average grade is: {int(avg_grade)}")   # to ignore the fractions




#   CASE SENSITIVE LOOK UP - CAN BE DONE EASIER, SO FAR MY ONLY SOLUTION
# countries_visited =['Turkey', 'Germany', 'USA', 'France', 'Italy', 'Saudi Arabia', 'Maldives']
# country_input = input('Please enter a country name you visited so far:')
#
# been_there = False
# for country in countries_visited:
#     if country.upper() == country_input.upper():
#         print('Well, I have been there')
#         been_there = True
#
# if not been_there:
#     print('Never been there!')



# user_input = input('Do you wish to continue? yes/no')
#
# while user_input == 'yes':
#     print('We are running the program')
#     user_input = input('Do you wish to continue? yes/no')
#
# print('We stopped running')




print('Welcome to the countries app!')

countries_visited = []
print(f'So far you have visited {len(countries_visited)} countries. ')

usr_input = ''

while usr_input != 'q':
    usr_input = input('Please enter a to add a country name you visited, q to quit and l to list the countries you visited so far : \n')
    if usr_input == 'a':
        country_name = input('Please enter where you have been')
        countries_visited.append(country_name)
    elif usr_input == 'l':
        print(f'So far you have visited these countries: {countries_visited} ')

print('Program quited per your request!')

