from menu import *
class Restaurent:
    employees = []
    menu = Menu()
    def __init__(self,name):
        self.name = name
    
    def add_employee(self,employee):
        self.employees.append(employee)
    
    def view_employee(self):
        print("Employee List : ")
        for emp in self.employees:
            print(f"Name: {emp.name}, Phone: {emp.phone}, Email: {emp.email}. Address: {emp.address}")
        