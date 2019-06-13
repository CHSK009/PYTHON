class employee:
    empcount = 0
    salary = []

    def __init__(self, name, family, salary, dept):
        self.salary = salary
        self.name = name
        self.family = family
        self.dept = dept
        employee.empcount += 1
        employee.salary.append(self.salary)

    def avg_salary(self):
        sum = 0
        for salary in employee.salary:
            sum += salary
            avgsal = sum / employee.empcount
        return avgsal


emp1 = employee("gautam","software",100000,"webdev")
emp2 = employee("kranthi","sports",100000,"cricket")
emp3=employee("sk","gamer",130000,"creative")
print(emp1.avg_salary())
class fulltime(employee):
    def __init__(self,name,family,salary,dept):
        employee.__init__(self,name,family,salary,dept)
        self.type="fulltime"
emp4=fulltime("sk","gamer",130000,"creative")
print(emp4.type)