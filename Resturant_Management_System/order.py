class Order:
    items = {}
    def add_item(self,item):
        if item in self.items:
            self.items[item] += item.quantity
        else:
            self.items[item] = item.quantity
    
    def remove_item(self,item):
        if item in self.items:
            del self.items[item] 
            print("Product Removed Successfully")
    
    def total_price(self):
        total = 0
        for item, quantity in self.items.items():
            total +=quantity * item.price  
        print(f"Total Price : {total} tk")

    
    def clear(self):
        self.items = {}