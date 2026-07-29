from abc import ABCMeta, abstractstaticmethod, abstractmethod

class IDepartment(metaclass=ABCMeta):

    @abstractmethod
    def __init__(self, employees):
        """ Implement in child class """

    @abstractstaticmethod
    def print_department(self):
        """ Implement it in child class """


class Accounting(IDepartment):

    def __init__(self, employees):
        self.employees = employees

    def print_department(self):
        print(f"Accounting Employees: {self.employees}")


class Development(IDepartment):

    def __init__(self, employees):
        self.employees = employees

    def print_department(self):
        print(f"Development Employees: {self.employees}")


class ParentDepartment(IDepartment):

    def __init__(self, employees):
        self.employees = employees
        self.base_employees = employees
        self.sub_departments = []

    def add(self, dept):
        self.sub_departments.append(dept)
        self.employees += dept.employees

    def print_department(self):
        print(f"Parent Department Employees: {self.employees}")
        for dept in self.sub_departments:
            dept.print_department()
        print(f"Total number of employees: {self.employees}")


dept1 = Accounting(200)
print(dept1.print_department())

dept2 = Development(300)
print(dept2.print_department())

parent_dept = ParentDepartment(50)

parent_dept.add(dept1)
parent_dept.add(dept2)

print(parent_dept.print_department())

