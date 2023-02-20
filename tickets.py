from ticket_data import Settings
from ticket import Ticket
from receipt import Receipt
from create_ticket import create_ticket
import ticket_formulas as tf

"""Setup the settings and ask for the amount of people"""
ts = Settings()

tickets = []
ts.amount_costumers = int(input('For how many people do you want to buy tickets? '))

"""Start the loop based on the amount of people"""
i = ts.amount_costumers
while i > 0:
    age_input = int(input('\nwhat is the age of this individual? '))

    # Create an individual ticket based on the age you've given and
    # add it to all the other tickets
    ticket = Ticket(ts, age_input)
    tickets.append(ticket)

    # Add the ticket price to the total amount and add print both the total and individual price
    ts.total_price += ticket.price
    print('the tickets price = ' + '{:.2f}'.format(ticket.price))
    print('the current total price = ' + '{:.2f}'.format(ts.total_price))

    i -= 1

"""Look if there are more than 5 people. If so, give a group discount"""
if len(tickets) >= 5:
    ts.group_discount = True

"""Ask if the costumer wants parking tickets"""
answer = input('Do you want parking tickets? (y/n):  ')
if answer == 'y':
    ts.amount_parking_tickets = int(input('how many? '))
    ts.price_for_parking = tf.add_parking(ts, ts.amount_parking_tickets)
    ts.total_price += ts.price_for_parking

"""Quantify the total discount and total price and print them"""
# Discount:
ts.total_discount = 0
for ticket in tickets:
    ts.total_discount += ticket.discount
if ts.group_discount:
    ts.total_discount += ts.people_discount

# Price:
if ts.group_discount:
    ts.total_price -= ts.people_discount


# Rounding everything to two decimals
total_price = '{:.2f}'.format(ts.total_price)
total_discount = '{:.2f}'.format(ts.total_discount)
tf.rounding_setup(ts)
for ticket in tickets:
    ticket.update_rounding()

# Creating the tickets:
for ticket in tickets:
    create_ticket(ts, ticket)
receipt = Receipt(ts)
# Restoring used codes
ts.append_code_data()

# Printing discount and prices
print('----------------------------------------------------------------------------------------')
for ticket in tickets:
    print(f'Entrance ticket: ${ts.base_price} base price - ${ticket.discount} age discount = ${ticket.price}')
if ts.amount_parking_tickets > 0:
    print(f'Parking tickets: {ts.amount_parking_tickets} x ${ts.price_parking_ticket} = ${ts.price_for_parking}')
if ts.group_discount:
    print(f"Because you bought more than {ts.amount_costumers_discount} tickets, "
          f"you get an ${ts.people_discount} discount")
print(f'Your total discount: ${total_discount}')
print(f'Your total price: ${total_price}')



