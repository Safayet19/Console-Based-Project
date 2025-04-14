from users import *
from menu import *
from customer import *

rest_name = Restaurent("KFC Lite")
def customer_menu():
        name = input("Enter your name: ")
        email = input("Enter your mail: ")
        phone = input("Enter Phone Number: ")
        address = input("Enter Address: ")
        customer = Customer(name = name,email = email,phone = phone,address=address)
        while(True):
            print(f"**********Welcome {customer.name} **********")
            print("1. View Menu")
            print("2. Add item to the cart")
            print("3. View Cart")
            print("4. Paybill")
            print("5. Exit")
            
            choice = input("Enter Your Choice: ")
            if(choice == "1"):
                customer.view_items(rest_name)
            elif(choice == "2"):
                item_name = input("Enter Item Name: ")
                qnt = int(input("Enter total quantity: "))
                customer.add_to_cart(rest_name,item_name,qnt)
            elif(choice == "3"):
                customer.view_cart()
            elif(choice == "4"):
                customer.pay_bill()
            elif(choice == "5"):
                break
            else:
                print("Invalid Choice!")
                

def admin_menu():
    name = input("Enter your name: ")
    email = input("Enter your mail: ")
    phone = input("Enter Phone Number: ")
    address = input("Enter Address: ")
    admin = Admin(name = name,email = email,phone = phone,address=address)
    while(True):
        print(f"**********Welcome {admin.name} **********")
        print("1. Add New Item")
        print("2. Add New Employee")
        print("3. View Employee")
        print("4. View Items")
        print("5. Delete Items")
        print("6. Exit")
        
        choice = input("Enter Your Choice: ")
        if(choice == "1"):
            item_name = input("Enter item name: ")
            item_price = int(input("Enter Price: "))
            item_qnt = int(input("Enter Quantity: "))
            item = FoodItems(item_name,item_price,item_qnt)
            admin.add_item(rest_name,item)
        
        elif(choice == "2"):
            name = input("Enter Employee Name: ")
            phone = input("Enter Employee Phone: ")
            email = input("Enter Email: ")
            designation = input("Enter Employee Designation: ")
            age = input("Enter Employee age: ")
            salary = input("Enter Employee salay: ")
            address = input("Enter Employee Address: ")
            
            employee = Employee(name,phone,email,address,age,designation,salary)
            admin.add_employee(rest_name,employee)
            
        elif(choice == "3"):
            admin.view_employee(rest_name)
        elif(choice == "4"):
            admin.view_items(rest_name)
        elif(choice == "5"):
            item_name = input("Enter Item: ")
            admin.delete_item(rest_name,item_name)
        elif(choice == "6"):
            break
        else:
            print("Invalid Choice!")

def main_menu():
    while(True):
        print("****************Welcome to KFC Lite's Restaurent****************")
        print("1. Customer")
        print("2. Admin")
        print("3. Exit")
        choice = input("Enter Your Choice: ")
        if(choice == "1"):
            customer_menu()
        elif (choice == "2"):
            admin_menu()
        elif (choice == "3"):
            break
        else:
            print("Invalid Choice")

main_menu()