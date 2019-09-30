class Customer:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_customer_details(self):
        print(f"Customer Info: \nname: {self.name}\nage: {self.age}")


class ChildCustomer(Customer):
    # pass  #Use the pass keyword when you do not want to add any other properties or methods to the class.
    def __init__(self, name_c, age_c, member_since):
        Customer.__init__(self, name_c, age_c)
#        super().__init__(name_c, age_c)  #super() -> child class inherit all the methods and properties from its parent
        self.member_since = member_since

    def thank_customer(self):
        print("Thank you for being a customer since", self.member_since)


c1 = Customer("Philip", 43)

# c1.show_customer_details()
# c1.name = "Philipa"
# c1.show_customer_details()
# del c1.age  # deletes the age attribute of the c1 object. del c1 completely deletes the c1 object.
# c1.age = 46  # reassigning age attribute of the c1 object after deleting it

c1.show_customer_details()

c2 = ChildCustomer("Jane", 21, 2015)
c2.show_customer_details()
c2.thank_customer()

