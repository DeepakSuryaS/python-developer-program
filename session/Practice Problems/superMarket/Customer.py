import SuperMarket as sm

class Customer:
    def __init__(self, c_id, c_name, c_contact, c_cart = {}):
        self.c_id = c_id
        self.c_name = c_name
        self.c_contact = c_contact
        self.c_cart = c_cart

    def add_to_cart(self, product, quantity):
        if product in self.c_cart:
            self.c_cart[product] += quantity
        else:
            self.c_cart.setdefault(product, quantity)

    def remove_from_cart(self, product):
        if product in self.c_cart:
            id = product.p_id
            self.c_cart.pop(product)
            return id

    def req_bill(self):
        return sm.SuperMarket.calc_bill(self.c_cart)
