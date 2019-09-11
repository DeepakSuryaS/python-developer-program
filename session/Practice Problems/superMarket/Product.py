class Product:
    def __init__(self, p_id, p_name, unit_price, total_quantity, offer = None):
        self.p_id = p_id
        self.p_name = p_name
        self.p_price = unit_price
        self.p_quantity = total_quantity
        self.p_offer = offer

    def remove_product(self):
        id = self.p_id
        del self
        return id

    def change_price(self, price):
        self.p_price = price

    def update_stock(self, current_quantity):
        self.p_quantity = current_quantity

    def __str__(self):
        return "{} {}".format(self.p_id, self.p_name)

    def add_offer(self, offer):
        if self.p_id == offer.p_id:
            self.offer = offer
