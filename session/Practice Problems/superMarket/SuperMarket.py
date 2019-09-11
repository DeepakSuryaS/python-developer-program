class SuperMarket:
    @classmethod
    def calc_bill(cls, cart):
        total_amount = 0
        for product, quantity in cart.items():
            if(product.p_offer != None):
                offer_avail = quantity // product.offer.offer_quantity
                offer_price = offer_avail * product.offer.offer_price
                remain_quantity = quantity % product.offer.offer_quantity
                remain_price = remain_quantity * product.p_price
                total_amount += offer_price + remain_price
            else:
                total_amount += product.p_price * quantity

            product.update_stock(product.p_quantity - quantity)

        total_amount += total_amount * 0.05
        
        return total_amount
