class Adminstaff():
    def __init__(self,role):
        self.role = role
        print("adminstaff created at level 1")


class Employee(Adminstaff):
    start_time = "10 am "
    end_time = "5 pm"
    def __init__(self,role):
        super().__init__(role)
        print("employee created at level 2")

class Accoountant(Employee):
    def __init__(self, salary, role):
        super().__init__(role)
        self.salary = salary
        
        
acct1 = Accoountant(25000, "ca")

print(acct1.role,acct1.salary,acct1.start_time,acct1.end_time)
