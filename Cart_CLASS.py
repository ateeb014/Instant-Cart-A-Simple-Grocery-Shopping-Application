class SmartCart(dict):
    '''dict subclass to maintain user cart'''

    def add_item(self, item, quantity):
        # Add item to the cart, using item as key and quantity as value
        self[item] = self.get(item, 0) + quantity

    def get_items(self):
        # Return all items in the cart
        return self.items()

    def get_subtotal(self):
        total = 0
        # Calculate subtotal by iterating over items and multiplying price with quantity
        for item, quantity in self.items():
            total += item.get_price() * quantity
        return total

    def subtotal(self):
        '''Returns subtotal from a dictionary object'''
        total = 0
        # Calculate subtotal by iterating over items and multiplying price with quantity
        for item in self.keys():
            total += item.get_price() * self[item]
        return total


class Item(object):
    '''Item class defines an item
    available in store. Item object saved in
    lists per category'''
    dairy_items = []  # list of all dairy items
    veg_fruit_items = []  # list of  veg and fruit items
    meat_items = []  # list of  meat and poultry items
    seafood_items = []  # list of seafood items

    def __init__(self, category, name, price, unit):
        '''Initialization method'''
        self.__category = category.lower()

        self.__name = name
        self.__price = price
        self.__unit = unit
        # initialize name, price and unit as private method

        if self.__category == 'dairy'.lower():
            Item.dairy_items.append(self)
        elif self.__category == 'vegetable' or self.__category == 'fruit':
            Item.veg_fruit_items.append(self)
        elif self.__category == 'meat' or self.__category == 'poultry':
            Item.meat_items.append(self)
        elif self.__category == 'seafood':
            Item.seafood_items.append(self)

    def get_category(self):
        return self.__category

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_unit(self):
        return self.__unit

    # define four get methods
    # to return four private attributes

    def __str__(self):
        line = '{}, {}, {}, {}'.format(self.get_category(), self.get_name(),
                                       self.get_price(), self.get_unit())
        return line


# process file
# open file, read information, create Item object
products = []
f = open('input_data.txt', 'r')
content = f.readlines()
for line in content:
    line2 = line.strip().split("|")
    item = Item(line2[1], line2[0], float(line2[2]), line2[3])


f.close()

'''
Testing code to check object creation per category list
Comment out when done. After successful completion
of class, the following code will print each item in the input file
'''

""""

for item in Item.dairy_items:
    print(item)
print('++++++++++')

for item in Item.veg_fruit_items:
    print(item)
print('++++++++++')


for item in Item.meat_items:
    print(item)
print('++++++++++')


for item in Item.seafood_items:
    print(item)
print('++++++++++')

"""
