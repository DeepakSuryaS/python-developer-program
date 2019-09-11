import Product as product
import Customer as customer
import Offers as offer

p1 = product.Product(111, 'A', 50, 500)
p2 = product.Product(222, 'B', 30, 50)
p3 = product.Product(333, 'C', 20, 500)

offer_1 = offer.Offers(11, 101, 3, 120, '4/Jan/2020')
offer_2 = offer.Offers(12, 102, 2, 45, '23/sept/2020')

p1.add_offer(offer_1)
p2.add_offer(offer_2)

c1 = customer.Customer(1, 'ABC', "+919999999")

c1.add_to_cart(p1, 3)
c1.add_to_cart(p2, 2)
c1.add_to_cart(p1, 2)
c1.add_to_cart(p3, 1)

print(c1.req_bill())
print(p1)
print(p2)
print(p3)
