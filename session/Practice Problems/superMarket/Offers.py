class Offers:
    def __init__(self, offer_id, p_id, offer_quantity, offer_price, validity):
        self.offer_id = offer_id
        self.p_id = p_id
        self.offer_quantity = offer_quantity
        self.validity = validity

    def remove_offer(self):
        id = self.id
        del self
        return id

    def update_offer_quantity(self, quantity):
        self.offer_quantity = quantity

    def update_offer_price(self, price):
        self.offer_price = price
