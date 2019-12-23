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

class Developer(Employee):
    increment = 1.06

    def __init__(self, first_name, last_name, email, payment, prog_lang):
        super().__init__(first_name, last_name, email, payment)
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self, first_name, last_name, email, payment, employees = None):
        super().__init__(first_name, last_name, email, payment)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_employee(self):
        for emp in self.employees:
            print('--> ',emp.full_name())


dev_one = Developer("Newaz", "Sharif", "newazsharif.dsi@gmail.com", 12000, "Java")
# print(dev_one.__dict__)

dev_two = Developer("Dev2", "Sharif", "dev2sharif.dsi@gmail.com", 10000, "Python")
# print(dev_two.__dict__)

dev_three = Developer("Dev3", "Sharif", "dev3sharif.dsi@gmail.com", 20000, "C++")
# print(dev_three.__dict__)


mgr_one = Manager("General", "Manager", "gm.dsi@gmail.com", 62000, [dev_one,dev_two])
# mgr_one.print_employee()

mgr_one.add_employee(dev_three)
mgr_one.print_employee()

mgr_one.remove_employee(dev_one)
mgr_one.print_employee()

#instance check
print(isinstance(mgr_one, Manager))
print(isinstance(mgr_one, Employee))
print(isinstance(mgr_one, Developer))


#Subclass check
print(issubclass(Manager, Developer))
print(issubclass(Manager, Employee))