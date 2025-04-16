#Create a class

class Product:
    """Represent a product in the inventory"""
    def __init__(self,name,price,qty,safestock):    #default initilize when creating a class
        self.name = name   #create attribute using specific to an instance
        self.price = price
        self.qty = qty       
        self.safestock = safestock

# Read current info of a product
    def get_product_info(self):  
        """Returns a formatted string with the product's information."""  
        return f"✅Product: {self.name}. Price: {self.price:.3f}. Quantity:{self.qty}. Safety stock: {self.safestock}"


# Auto restock
    def restock(self):   #not required parameter because it's a calculated value
        if self.qty < self.safestock:
            needed_amount = self.safestock-self.qty     #calculate needed restock qty
            self.qty += needed_amount
            return f"✅Safety restock {needed_amount} for product {self.name}. Current quantity: {self.qty}"
            # print(needed_amount)
        else:
            self.needed_amount = 0

#Sell: 
    def sell(self,amount):
        if amount <= self.safestock:
            self.qty -= amount
            return f"✅Order: {amount}. Deliver {amount} for product {self.name}. The rest quantity:{self.qty}"        
        else:
            sell_restock = amount - self.safestock
            self.qty = self.safestock + sell_restock - amount
            return f"✅Order: {amount}. Not enoungh!! Restock {sell_restock}. Deliver {amount} for product {self.name}. The rest quantity:{self.qty}"    
        
#Adjust price by qty: auto increase the price basing on stock
    def adjust_price_by_qty (self):
        if self.qty<=1/3*self.safestock:
            price_increase_percentage = 0.1
            increase_price = self.price * price_increase_percentage
            self.price*=(1+price_increase_percentage)
            return f"✅ Low stock warning: {self.name} stock is below 1/3 of safety stock, price increased {increase_price:.3f}. New price is {self.price:.3f}."
        if self.qty >= 1.5*self.safestock:
            price_decrease_percentage = 0.1
            decrease_price = self.price * price_decrease_percentage
            self.price*=(1-price_decrease_percentage)
            return f"✅ High stock warning: {self.name} stock is over 1/2 of safety stock, price decreased {decrease_price:.3f}. New price is {self.price:.3f}."
        else:
            return f"✅ Price is still stable."
        

#Create an instance of Product
p1=Product("Chair",130.99,20,100)
p2=Product("Bed",650.49,150,20)
p3=Product("Lamp",28.49,78,200)
p4=Product("Cabinet",335.99,47,20)

#Restocking & selling
print(p1.get_product_info())
print(p1.sell(5))
print(p1.restock())     # Check to see if restocking is needed for chairs
print(p1.sell(120))     # Attempt to sell 120 chairs, should trigger restocking  
print(p1.restock())     # Check to see if restocking is needed for chairs
print(p1.sell(90))     # Attempt to sell 120 chairs, should trigger restocking 
print(p1.adjust_price_by_qty())     # Trigger price adjustment 

print(p2.get_product_info())
print(p2.adjust_price_by_qty()) 