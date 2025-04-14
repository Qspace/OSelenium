#Create a class

class Product:
    """Represent a product in the inventory"""
    def __init__(self,name,qty,price,safestock):    #default initilize when creating a class
        self.name = name   #create attribute using specific to an instance
        self.qty = qty       
        self.price = price
        self.safestock = safestock

# Auto restock
    def restock(self):   #not required parameter because it's a calculated value
        if self.qty < self.safestock:
            needed_amount = self.safestock-self.qty     #calculate needed restock qty
            self.qty += needed_amount
            return f"Safety restock {needed_amount} for product {self.name}."
            # print(needed_amount)
        else:
            self.needed_amount = 0

#Sell   
    def sell(self,amount):
        if amount <= self.safestock:
            self.qty -= amount
            return f"Order: {amount}. Deliver {amount} for product {self.name}. The rest quantity:{self.qty}"        
        else:
            sell_restock = amount - self.safestock
            self.qty = self.safestock + sell_restock - amount
            return f"Order: {amount}. Not enoungh!! Restock {sell_restock}. Deliver {amount} for product {self.name}. The rest quantity:{self.qty}"    
        

#Create an instance of Product
p1=Product("Chair",20,130.99,100)
p2=Product("Bed",150,650.49,20)
p3=Product("Lamp",78,28.49,200)
p4=Product("Cabinet",47,335.99,20)

#Restocking & selling
# print(p1.sell(5))
print(p1.restock())     # Check to see if restocking is needed for chairs
print(p1.sell(120))     # Attempt to sell 120 chairs, should trigger restocking  
print(p1.restock())     # Check to see if restocking is needed for chairs
print(p1.sell(50))     # Attempt to sell 120 chairs, should trigger restocking  
