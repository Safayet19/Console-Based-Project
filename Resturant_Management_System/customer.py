from users import *
from order import *

class Customer(User):
    cart = Order()
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
    
    def view_items(self,restaurent):
        restaurent.menu.view_items()
    
    def add_to_cart(self, restaurent, item_name, quantity):
        item = restaurent.menu.find_item(item_name)

        if item:
            if quantity > item.quantity:
                print("Quantity Exceed !")
            else:
                item.quantity = quantity  # Update quantity
                self.cart.add_item(item)  # Add item to the cart (ensuring price stays)
                print(f"Successfully added {quantity} {item.name} to the cart")
        else:
            print("Item not found!")
    
    def view_cart(self):
        print("Name\tPrice\tQuantity")
        for item, quantity in self.cart.items.items(): 
            print(f"{item.name}\t{item.price * quantity}\t  {quantity}")
    
    def pay_bill(self):
        print(f"Total {self.cart.total_price} paid successfully !")
        self.cart.clear()
        
    




            
            
       