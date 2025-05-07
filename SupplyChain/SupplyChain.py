import pandas as pd  

class Product:  
    """Represent a product in the inventory"""  
    def __init__(self, name, price, qty, safestock):  
        self.name = name  
        self.price = price  
        self.qty = qty  
        self.safestock = safestock  

    def get_product_info(self):  
        return f"✅Product: {self.name}. Price: {self.price:.3f}. Quantity: {self.qty}. Safety stock: {self.safestock}"  

    def restock(self):  
        if self.qty < self.safestock:  
            needed_amount = self.safestock - self.qty  
            self.qty += needed_amount  
            return f"✅Safety restock {needed_amount} for product {self.name}. Current quantity: {self.qty}"  
        else:  
            return f"✅No restock needed for product {self.name}."  

    def sell(self, amount):  
        if amount <= self.safestock:  
            self.qty -= amount  
            return f"✅Order: {amount}. Deliver {amount} for product {self.name}. The rest quantity: {self.qty}"  
        else:  
            sell_restock = amount - self.safestock  
            self.qty = self.safestock + sell_restock - amount  
            return f"✅Order: {amount}. Not enough!! Restock {sell_restock}. Deliver {amount} for product {self.name}. The rest quantity: {self.qty}"  

    def adjust_price_by_qty(self):  
        if self.qty <= 1/3 * self.safestock:  
            price_increase_percentage = 0.1  
            increase_price = self.price * price_increase_percentage  
            self.price *= (1 + price_increase_percentage)  
            return f"✅ Low stock warning: {self.name} stock is below 1/3 of safety stock, price increased {increase_price:.3f}. New price is {self.price:.3f}."  
        if self.qty >= 1.5 * self.safestock:  
            price_decrease_percentage = 0.1  
            decrease_price = self.price * price_decrease_percentage  
            self.price *= (1 - price_decrease_percentage)  
            return f"✅ High stock warning: {self.name} stock is over 1/2 of safety stock, price decreased {decrease_price:.3f}. New price is {self.price:.3f}."  
        else:  
            return f"✅ Price is still stable."  

def main():  
    # Create product instances  
    p1 = Product("Chair", 130.99, 20, 100)  
    p2 = Product("Bed", 650.49, 150, 20)  

    results = []  
    results.append(p1.get_product_info())  
    results.append(p1.sell(5))  
    results.append(p1.restock())  
    results.append(p1.sell(120))  
    results.append(p1.restock())  
    results.append(p1.sell(90))  
    results.append(p1.adjust_price_by_qty())  
    results.append(p2.get_product_info())  
    results.append(p2.adjust_price_by_qty())  

    # Convert results list to DataFrame  
    df = pd.DataFrame({"Results": results})  

    # Save to Excel file  
    filepath = "SupplyChain.xlsx"  
    df.to_excel(filepath, index=False)  

    print(f"Results written to {filepath}")  

if __name__ == "__main__":  
    main()  