class FoodItems:
    def __init__(self,name,price,quanity):
        self.name = name
        self.price = price
        self.quantity = quanity

class Menu:
    items = []
    
    def add_item(self,item):
        self.items.append(item)
        print("Item added Successfully !")
    
    def find_item(self,item_name):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                return item
        return None
    
    def delete_item(self,item_name):
        item = self.find_item(item_name)
        if item:
            self.items.remove(item)
            print("Item Removed !")
        else:
            print("Item not found !")
    
    def view_items(self):
        print("Name\tPrice\tQuantity")
        for item in self.items:
            print(f"{item.name}\t{item.price}\t  {item.quantity}")
        