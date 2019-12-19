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
    pass

dev_one = Developer("Newaz", "Sharif", "newazsharif.dsi@gmail.com", 12000)

print(dev_one.full_name())
print(dev_one.payment)
dev_one.apply_raise()
print(dev_one.payment)

