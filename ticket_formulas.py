from random import randint


# Create a random 4 number code and check it to a database, so no duplicates get created
def create_code(td):
    while True:
        code = randint(1000, 9999)
        for sample in td.codes:
            if code == sample:
                continue
        td.codes.append(code)
        return code


# Simple formula to calculate the total amount of money spend on parking
def add_parking(ts, amount):
    i = amount
    total_parking = 0
    while i > 0:
        total_parking += ts.price_parking_ticket
        i -= 1
    return total_parking


# Round anything to 2 decimals
def round_currency(amount):
    cost = "{:.2f}".format(amount)
    return cost


# Round specific variables to 2 decimals
def rounding_setup(td):
    td.price_young = round_currency(td.price_young)
    td.base_price = round_currency(td.base_price)
    td.price_old = round_currency(td.price_old)
    td.price_parking_ticket = round_currency(td.price_parking_ticket)
    td.people_discount = round_currency(td.people_discount)
    td.price_for_parking = round_currency(td.price_for_parking)
