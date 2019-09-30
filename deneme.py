class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@loverdure.com'

    def printfullname(self):
        print(self.first + ' ' + self.last)


emp1 = Employee('Tugba', 'Alparslan', 7000)

Employee.printfullname(emp1)
emp1.printfullname()

# n1: int = int(input("Enter lower range :-\n"))

#for i in range(1, n1):
 #       print(i, i*2, i*i, i**i)

a = 2
a *= 3
print(a)

def unorganized(a, b):
    for i in range(a, b):
        print(i, i ** 2, i ** 3, i ** 4)

    # Function prints the organized set of values



#nBWE
def organized(a, b):
    for i in range(a, b):
        # Using formatters to give 6
        # spaces to each set of values
        print("{:6d} {:6d} {:6d} {:6d}"
              .format(i, i ** 2, i ** 3, i ** 4))

    # Driver Code


n1 = int(input("Enter lower range :-\n"))
n2 = int(input("Enter upper range :-\n"))

print("------Before Using Formatters-------")

# Calling function without formatters
unorganized(n1, n2)

print()
print("-------After Using Formatters---------")
print()

# Calling function that contain
# formatters to organize the data
organized(n1, n2)

print('*********************')

x = str(2)
y = 'sandwiches'
print(x + ' ' + y)



