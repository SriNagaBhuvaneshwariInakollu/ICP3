class Employee:
    empCount = 0
    sal=0

    def __init__(self, name, family, salary, dept):
        self.emp_name = name
        Employee.sal += salary
        #self.emp_sal = salary
        self.emp_family = family
        self.emp_dept = dept
        Employee.empCount += 1

    def displayCount(self):
        print "tot emp %d" % Employee.empCount

    def displayEmployee(self):
        print "Name:", self.emp_name, ", Sal:", self.sal, "Family:", self.emp_family, "Dept:", self.emp_dept




#class FulltimeEmployee(Employee):
   # def __init__(self, name, family, salary, dept, type):
        #Employee.__init__(name, family, salary, dept)


    def averageSalary(self):
        self.avgSalary = Employee.sal / Employee.empCount
        print ('The average salary of the employees is')
        print (self.avgSalary)


class FullTimeEmployee(Employee):
    def __init__(self):
        Employee.averageSalary(self)

emp1 = Employee("Sanju", "A", 10000, "CS")
emp2 = Employee("Vira", "B", 20000, "CT")
emp3 = Employee("Riya", "C", 30000, "EC")

emp1.displayEmployee()
emp2.displayEmployee()
emp3.displayEmployee()
print "tot emp %d" % Employee.empCount

x= FullTimeEmployee()







