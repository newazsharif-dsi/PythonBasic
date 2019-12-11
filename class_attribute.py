class Employee:
    """ class variable """
    increment = 1.04

    def __init__(self, first_name, last_name, email, payment):
        """ initialize instance variables """
        self.first_name = first_name;
        self.last_name = last_name;
        self.email = email;
        self.payment = payment;

    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def apply_raise(self):
        """ Access class attribute by instance """
        self.payment = self.payment * self.increment



#creating instances of Employee class
employee_one = Employee("Newaz", "Sharif", "newaz.sharif&xyz.com", 10000)
employee_two = Employee("Mohammad", "Ashraful", "md.ash&xyz.com", 20000)
print(employee_one.full_name())


print(employee_one.__dict__) #will print the namespace of employee_one instance
print(Employee.__dict__) #will print the namespace of Employee class and we will see the 'increment' attribute

employee_one.apply_raise()
print(employee_one.payment)

#Locally modifying 'increment' attribute
employee_one.increment = 1.05

print(Employee.increment)
print(employee_one.increment)
print(employee_two.increment)
