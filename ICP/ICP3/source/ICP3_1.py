"""
1. Create a class Employee and then do the following
Create a data member to count the number of Employees
Create a constructor to initialize name, family, salary, department
Create a function to average salary
Create a Fulltime Employee class and it should inherit the properties of Employee class
Create the instances of Fulltime Employee class and Employee class and call their member functions.

Scott McElfresh sme1d1 Deep Learning 2021 2/3/2021
"""


class Employee:
    count = 0
    salaryTotal = 0

    def __init__(self, n, f, s, d):
        Employee.count += 1
        Employee.salaryTotal = Employee.salaryTotal + s
        self.name = n
        self.family = f
        self.salary = s
        self.department = d

    def avg_salary(self):
        avgsal = float(Employee.salaryTotal) / Employee.count
        return avgsal

    def print_name(self):
        print(self.name)

    def print_family(self):
        print(self.family)

    def print_salary(self):
        print(self.salary)

    def print_department(self):
        print(self.department)


class FulltimeEmployee(Employee):
    def __init__(self, n, f, s, d):
        Employee.__init__(self, n, f, s, d)


a = Employee("Bill S.", "Preston, Esq.", 50000, "XLNT")
b = FulltimeEmployee("Ted 'Theodore'", "Logan", 100000, "XLNT")

a.print_name()
a.print_family()
a.print_salary()
a.print_department()
print("")
b.print_name()
b.print_family()
b.print_salary()
b.print_department()
print("")
print("Average salary of all employees: {}".format(a.avg_salary()))
