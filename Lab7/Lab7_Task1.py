class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def get_info(self):
        return f"{self.name}, {self.id}"

class Manager(Employee):
    def __init__(self, name, id, department):
        Employee.__init__(self, name, id)
        self.department = department
    def manage_project(self):
        return f"работает над проектом {self.department}"

class Technician(Employee):
    def __init__(self, name, id, speacialization):
        Employee.__init__(self, name, id)
        self.speacialization = speacialization
    def perform_maintenance(self):
        return f"{self.name}, выполнил обслуживание: {self.speacialization}"

class TechManager(Manager, Technician):
    def __init__(self,name,id,depart,special):
        Manager.__init__(self,name,id,depart)
        Technician.__init__(self,name,id,special)
        self.team = []
    def get_info(self):
        return "ИМЯ: {},ID : {}, проект : {} , специализация : {}" .format(self.name,self.id ,self.depart , self.special)
    def add_employee(self, employee):
        self.team.append(employee)
    def get_team_info(self):
        if not self.team:
            return "No team members."
        return "\n".join([emp.get_info() for emp in self.team])

emp1 = Employee("Akhmad123", "987")
tm1 = TechManager("Akhmad", "123", "dadada", "yeah")
tm1.add_employee(emp1)
print(tm1.get_team_info())