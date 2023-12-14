# import tkinter
# import Item and SmartCart class from CLASS file
# import tkinter as tk
from tkinter import *
from Cart_CLASS import Item
from Cart_CLASS import SmartCart
from functools import partial
import random
import string  # used in random receipt no function


class MyFrame(Frame):
    def __init__(self, root):
        '''Constructor method'''
        Frame.__init__(self, root)  # Frame class initialization
        self.init_container()  # initialize all widget containers

        # initialize SmartCart dict object - key = Item object item selected, value = quantity
        self.cart = SmartCart()
        self.welcome()  # start the application

        # Associated with subtotal label
        self.data = StringVar(self, 'Subtotal: 0.0')

    def init_container(self):
        '''Initialize widget containers'''
        self.quantity_entries = []  # qunatity entry list
        self.states = []  # holds state if selected/not i-th list item holds selection for i-th item

    def clear_frame(self):
        '''Clears the previous frame'''
        for widget in self.winfo_children():
            widget.destroy()

    def exit_application(self):
        '''Exits the program'''
        root.destroy()

    def welcome(self):
        '''1. Welcome window - refer spec file for details'''
        self.clear_frame()
        Label(self, text='****Welcome to Instant Cart!****',
              background="gray70").pack(side=TOP)

        # Start Ordering: Button – start the program, command
        Button(self, text='Start Ordering',
               command=self.shop_by_category).pack(side=TOP)

        # Exit Application: Button – exit the program, command = exit_application
        Button(self, text='Exit Application',
               command=self.exit_application).pack(side=TOP)

    def shop_by_category(self):
        '''2. Widget to display different category of items - refer spec file for details'''
        self.clear_frame()
        self.init_container()

        # a.	Choose Category: label
        Label(self, text='Choose Category:',
              background="gray70").grid(row=0, column=0)

        # b.	Dairy: Button
        self.dairy_button = Button(
            self, text='Dairy', command=partial(self.start, Item.dairy_items))
        self.dairy_button.grid(row=1, column=0)

        # c.	Vegetable and Fruit : Button
        self.veg_fruit_button = Button(
            self, text='Vegetable and Fruit', command=partial(self.start, Item.veg_fruit_items))
        self.veg_fruit_button.grid(row=2, column=0)

        # d.	Poultry and Meat: Button
        self.poultry_meat_button = Button(
            self, text='Poultry and Meat', command=partial(self.start, Item.meat_items))
        self.poultry_meat_button.grid(row=3, column=0)

        # e.	Seafood: Button
        self.seafood_button = Button(
            self, text='Seafood', command=partial(self.start, Item.seafood_items))
        self.seafood_button.grid(row=4, column=0)

        # f.	Go Back: Button
        # layout manager for all the widgets
        Button(self, text='Go Back', command=self.welcome).grid(
            row=5, column=0)

    def start(self, current_items):
        ''''3. Start ordering from selected category,
        list passed by command will be used as current_items'''
        self.clear_frame()
        self.init_container()

        # creating widgets for items using a for loop
        Label(self, text='Item').grid(row=0, column=0)
        Label(self, text='Price').grid(row=0, column=1)
        Label(self, text='Quantity').grid(row=0, column=2)
        Label(self, text='Unit').grid(row=0, column=3)

        # iterative over each item of current items and
        # create that many checkbutton, price and unit label,and quantity entry
        row = 1
        for item in current_items:
            # keeps track if an item is selected
            self.states.append(IntVar())
            checkbutton = Checkbutton(self, text=item.get_name(),
                                      variable=self.states[row - 1])
            checkbutton.grid(row=row, column=0)

            # create and layout a price label, set text to item.get_price()
            Label(self, text=item.get_price()).grid(row=row, column=1)

            # create and layout a quantity entry and append to quantity_entries, set width = 2
            quantity_entry = Entry(self, width=2)
            quantity_entry.grid(row=row, column=2)
            self.quantity_entries.append(quantity_entry)

            # create and layout unit_label and set text to item.get_unit() function
            Label(self, text=item.get_unit()).grid(row=row, column=3)
            row += 1

        # create and layout subtotal lable, set textvaribale = self.data so it changes
        # with each add_to_cart button being pressedng
        Label(self, textvariable=self.data).grid(
            row=row, column=0, columnspan=4)

        # create and layout select categories: button
        Button(self, text='Select Categories',
               command=self.shop_by_category).grid(row=row+1, column=0)

        # create and layout add_to_cart: Button
        Button(self, text='Add to Cart',
               command=partial(self.add_to_cart, current_items)).grid(row=row+1, column=1)
        # create and layout: checkout: Button
        Button(self, text='Checkout',
               command=self.checkout).grid(row=row+1, column=2)

    def add_to_cart(self, current_items):
        '''3. Added to cart, displays subtotal - see spec file for details layout'''
        # for i in range(len(current_items)):
        # get() the value of i-th item of self.states -> returns 1 if selected otherwise 0
        # if item is selected:
        # get the product quantity from quantity_entries using get() function
        # add item to self.cart dict where k = item object, v = quantity
        for i in range(len(current_items)):
            if self.states[i].get() == 1:
                quantity_str = self.quantity_entries[i].get()
                try:
                    quantity = int(quantity_str)
                    if quantity > 0:
                        item = current_items[i]
                        self.cart.add_item(item, quantity)
                except ValueError:
                    pass

        # set the StringVar to be the current subtotal (SmartCart object self.cart has subtotal method)
        # refer to class file
        self.data.set(f"Subtotal: {self.cart.subtotal()}")

    def get_receipt_number(self):
        '''Generate random receipt number'''
        return ''.join(random.choices(string.ascii_letters.upper() + string.digits, k=4))

    def checkout(self):
        '''4. Check out window '''
        self.clear_frame()
        # code  to create and layout following widgets:

        # refer to receipt frame
        receipt_frame = Frame(self)
        receipt_frame.pack(fill=BOTH, expand=True)

        # Your e-receipt: Label
        # Name Price Quantity Unit: Header Label
        header = Label(
            receipt_frame, text='Name      Price     Quantity   Unit')
        header.grid(row=0, column=0, columnspan=4, pady=10)

        # Item purchased, price quantity, unit: Label - from cart dictionary using self.cart.items()
        # Use self.cart.get_items() to get the dictionary
        cart_items = self.cart.get_items()
        row = 1
        for item, quantity in cart_items:  # Iterate directly over dictionary items
            name_label = Label(receipt_frame, text=item.get_name())
            price_label = Label(receipt_frame, text=f'${item.get_price():.2f}')
            quantity_label = Label(receipt_frame, text=quantity)
            unit_label = Label(receipt_frame, text=item.get_unit())
            name_label.grid(row=row, column=0, pady=5)
            price_label.grid(row=row, column=1, pady=5)
            quantity_label.grid(row=row, column=2, pady=5)
            unit_label.grid(row=row, column=3, pady=5)
            row += 1

        # Subtotal: Label - get self.cart subtotal - new label
        subtotal = self.cart.get_subtotal()
        subtotal_label = Label(
            receipt_frame, text=f'Subtotal: ${subtotal:.2f}')
        subtotal_label.grid(row=row, column=0, columnspan=2, pady=10)

        # Tax: Label - 4.3%
        tax = subtotal * 0.043
        tax_label = Label(receipt_frame, text=f'Tax (4.3%): ${tax:.2f}')
        tax_label.grid(row=row, column=2, columnspan=2, pady=10)
        row += 1

        # Total: Label - subtotal + tax
        total = subtotal + tax
        total_label = Label(
            receipt_frame, text=f'Total: ${total:.2f}', font='bold')
        total_label.grid(row=row, column=0, columnspan=4, pady=10)
        row += 1

        # ‘Thank you’ message: Label
        thank_you = Label(
            receipt_frame, text='Thank you for using instant cart!')
        thank_you.grid(row=row, column=0, columnspan=4, pady=10)

        # Exit application: Button – exit the program- command = exit_application
        exit_button = Button(
            receipt_frame, text='Exit Application', command=self.exit_application)
        exit_button.grid(row=row+1, column=0, columnspan=4, pady=10)

        # Receipt Number: Label - Randomly generated by program
        # receipt_number_label
        order_number = ''.join(random.choices(
            string.ascii_uppercase + string.digits, k=6))
        receipt_number_label = Label(
            receipt_frame, text=f'Receipt Number: {order_number}', background="gray70")
        receipt_number_label.grid(row=row+2, column=0, columnspan=4, pady=10)


# main driver code
# create root window
root = Tk()
root.title("Instant Cart")  # set window title

# create a myframe object and layout
myframe = MyFrame(root)
myframe.pack()

# call mainloop
root.mainloop()
