# Instant Cart - Grocery Shopping GUI

# Description
This project demonstrates a simple user cart for grocery shopping, implementing fundamental procedural and object-oriented concepts along with Graphical User Interface (GUI) techniques. The program reads item information from an input file, organizes items by category, and allows users to interact with a GUI for selecting and purchasing items.

# Project Structure

#Class File (Cart_CLASS.py):
1. Contains the SmartCart class and Item class.
2. SmartCart: A dict subclass managing cart items and quantities.
3. Item: Class variables for different item categories (Dairy, Vegetable, Fruit, Poultry, and Seafood).
4. Methods for retrieving category, name, unit, price, and displaying a string representation.

#GUI File (Cart_GUI.py):
1. Implements the graphical user interface for grocery shopping.
2. Main Menu: Welcome screen with start ordering and exit buttons.
3. Choose Category: Displays category options (Dairy, Vegetable and Fruit, Poultry, Seafood).
4. Select Category: Allows users to select items, enter quantities, and add to cart.
5. Checkout: Displays a summary of the purchase, including receipt information.

# Program Workflow
1.	Reads item information from an input file.
2.	Organizes items by category using the Item class.
3.	GUI allows users to start ordering, choose categories, select items, and add them to the cart.
4.	Checkout displays a summary of the purchase with a randomly generated receipt number.
