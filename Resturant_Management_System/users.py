from abc import ABC
from restaurent import *
from order import *

class User(ABC):
    def __init__(self,name,phone,email,address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address
    
class Employee(User):
    def __init__(self, name, phone, email, address,age,designation,salary):
        super().__init__(name, phone, email, address)
        self.age = age 
        self.designation = designation
        self.salary = salary

class Admin(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
    
    def add_employee(self, restaurent, employee):
        restaurent.add_employee(employee)
    
    def view_employee(self,restaurent):
        restaurent.view_employee()
    
    def add_item(self,restaurent,item):
        restaurent.menu.add_item(item)
    
    def delete_item(self,restaurent,item):
        restaurent.menu.delete_item(item)
    
    def view_items(self,restaurent):
        restaurent.menu.view_items()
        
