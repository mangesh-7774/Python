from payment_gateway import payment_gateway
from card_payment import card
from upi_payment import upi

pg = payment_gateway()


ip = int(input("Enter payment method : 1.Card 2.UPI \nEnter here :"))

if ip==1:
  pg.payment_process(upi())
elif ip==2:
  pg.payment_process(card())
else:
  print("Inavlid")  