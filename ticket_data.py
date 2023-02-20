class Settings:

    def __init__(self):
        """Static data"""
        # Price structure
        self.price_young = 5
        self.base_price = 10
        self.price_old = 8
        self.price_baby = 0
        self.price_parking_ticket = 7.5

        # Group discounts
        self.amount_costumers_discount = 5
        self.people_discount = 5

        # Age ranges
        self.min_young = 4
        self.max_young = 18
        self.min_old = 65

        """Variable data"""

        # Group costumers
        self.group_discount = False
        self.amount_costumers = 0
        self.amount_parking_tickets = 0
        self.price_for_parking = 0
        self.total_tickets = 0
        self.babies = 0
        self.children = 0
        self.grandparents = 0
        self.total_price = 0
        self.total_discount = 0

        # Code Data
        self.codes = []
        self.read_code_data()

        # Location library for receipt creation
        self.cell_data = [
            ['&_ticket#_&', ''],
            ['&_base_&', ''],
            ['&_old_&', ''],
            ['&_young_&', ''],
            ['&_babies_&', ''],
            ['&_base_discount_&', ''],
            ['&_base_total_&', ''],
            ['&_old_discount_&', ''],
            ['&_young_discount_&', ''],
            ['&_baby_discount_&', ''],
            ['&_parking#_&', ''],
            ['&_parking_&', ''],
            ['&_parking_total_&', ''],
            ['&_group_&', ''],
            ['&_total_discount_&', ''],
            ['&_total_&', ''],
            ['&_complete_&', ''],
            ['&_old_total_&', ''],
            ['&_young_total_&', ''],
            ['&_baby_total_&', ''],
            ['&_parking_desc_&', ''],
            ['&_group_desc_&', ''],
        ]

    """Reading a file with all the taken codes and appending to self.codes"""

    def read_code_data(self):
        filename = 'code_data.txt'
        with open(filename) as cd:
            for code in cd:
                sample = code.rstrip()
                self.codes.append(int(sample))

    """Rereading self.codes and updating code_data.txt with new codes"""

    def append_code_data(self):
        filename = 'code_data.txt'
        with open(filename, 'w') as cd:
            for code in self.codes:
                cd.write(f'{code}\n')
