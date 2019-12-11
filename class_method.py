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

    """ class method """
    @classmethod
    def set_increment(cls, amount):
        cls.increment = amount

    """ Alternative constructor using class method """
    @classmethod
    def create_employee(cls, str):
        first_name, last_name, email, payment = str.split("-")
        return cls(first_name, last_name, email, payment)


employee_one = Employee("Newaz", "Sharif", "newaz.sharif&xyz.com", 10000)
employee_two = Employee("Mohammad", "Ashraful", "md.ash&xyz.com", 20000)

print(Employee.increment)
print(employee_one.increment)
print(employee_two.increment)

#Apply increment globally
Employee.set_increment(1.06)

print(Employee.increment)
print(employee_one.increment)
print(employee_two.increment)


str = "First-Last-abc@xyze-1000"
employee_three = Employee.create_employee(str) #instance created by alternative constructor
print(employee_three.full_name())
