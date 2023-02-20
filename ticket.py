import ticket_formulas as tf

'''Setup the ticket class'''
class Ticket:

    def __init__(self, td, age):
        # Setting up the individual variables needed for the ticket
        self.code = None
        self.price = None
        self.discount = 0
        self.age = age
        # Creating a code between 1000 and 9999
        self.code = tf.create_code(td)
        # Calculating the price based on the individuals age
        self.price_calc(td)

    def price_calc(self, td):
        # For every price category, check whether the given age falls with the range
        if self.age < td.min_young:
            self.price = 0
            td.babies += 1
        elif td.min_young <= self.age <= td.max_young:
            self.price = td.price_young
            td.children += 1
        elif td.max_young < self.age < td.min_old:
            self.price = td.base_price
        elif self.age >= td.min_old:
            self.price = td.price_old
            td.grandparents += 1
        # Increase the amount of tickets printed
        td.total_tickets += 1
        # Calculate the individuals discount
        discount = td.base_price - self.price
        self.discount += discount

    def print_price(self):
        print(self.price)

    def update_rounding(self):
        # Round prices to 2 decimals
        self.price = tf.round_currency(self.price)
        self.discount = tf.round_currency(self.discount)
