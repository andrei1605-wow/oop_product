class Product():
    inventory = []
    product_counter = 0

    def __init__(self, product_id, name, category, quantity, price, supplier):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.quantity = quantity
        self.price = price
        self.supplier = supplier
#method for adding product
    @classmethod
    def add_product(cls, name, category, quantity, price, supplier):
        cls.product_counter += 1
        new_product = Product(cls.product_counter, name, category, quantity, price, supplier)
        cls.inventory.append(new_product)
        return "Product added successfully"
#method for updating product
    @classmethod
    def update_product(cls, product_id, quantity=None, price=None, supplier=None):
        for product in cls.inventory:
            if product.product_id == product_id:
                if quantity is not None:
                    product.quantity = quantity
                if price is not None:
                    product.price = price
                if supplier is not None:
                    product.supplier = supplier
                return "Product information updated successfully"
        return "Product not found"
#method for deleting product
    @classmethod
    def delete_product(cls, product_id):
        for product in cls.inventory:
            if product.product_id == product_id:
                cls.inventory.remove(product)
            return "Product deleted successfully"
        return "Product not found"
    
class Order:
    def __init__(self, order_id, product_id, quantity, customer_info = None):
        self.order_id = order_id
        self.product_id = product_id
        self.quantity = quantity
        self.customer_info = customer_info

    #Method to place order
    def place_order(self):
        for product in Product.inventory:
            if product.product_id == self.product_id:
                if product.quantity >= self.quantity:
                    return "Order placed successfully. Order ID:{self.order_id}"
                else:
                    return "Insufficient stock to place order"
                return "Product not found"

p1 = Product.add_product("Laptop", "Electronics", 50, 1000, "Supplier A")
print(p1)
p4 = Product.add_product("T-Shirt", "Clothing", 100, 25, "Supplier B")
print(p4)
p2 = Product.update_product(1, quantity=45, price=950)
print(p2)
p3 = Product.delete_product(1)
print(p3)
order1 = Order(order_id=1, product_id=1, quantity=2, customer_info="John Doe")
print(order1.place_order())
