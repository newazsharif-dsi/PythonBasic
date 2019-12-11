class Employee:

    def __init__(self, first_name, last_name, email, payment):
        self.first_name = first_name;
        self.last_name = last_name;
        self.email = email;
        self.payment = payment;


    """ This is no instance or the class as first argument"""

    @staticmethod
    def isWorkDay(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


import datetime

my_date = datetime.date(2019, 12, 14)

print(Employee.isWorkDay(my_date))