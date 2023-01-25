class Person:
    def __init__(self, fname, lname):
        self._first_name = fname
        self._last_name = lname

    def print(self):
        print(f'Full name: {self._first_name} {self._last_name}')
    
    
    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, new_first_name):
        self._first_name = new_first_name


class Customer(Person):
    def __init__(self, fname, lname, postcode):
        self._address = postcode
        super().__init__(fname, lname)

    def print(self):
        print(f'Address: {self._address}', end='')
        super().print()


class Employee(Person):
    def __init__(self,fname, lname, employee_id):
        super().__init__(fname, lname)
        self.employee_id = employee_id 

    def print(self):
        print(f'employee {self.first_name} {self._last_name}\'s id number is: {self.employee_id}')



gary = Person('Gary', 'Anderson')
customer_gary = Customer('Gary', 'Anderson', 'HA7 9LP')
customer_gary.print()
employee_simon = Employee('Simon', 'Chadwick', 99234)
employee_simon.print()  