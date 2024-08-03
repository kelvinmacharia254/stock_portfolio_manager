"""
Do the necessary importation statement and experiment with the stock portfolio manager

Comment out print statement and run each at a time to understand behavior

"""
import stock_portfolio_manager
from stock_portfolio_manager import stock_portfolio_tracker as spt

# Retrieve the package doctring
# print(stock_portfolio_manager.__doc__)
# Retrieving the whole module docstring
# print(spt.__doc__)

# # Retrieving the Portfolio class docstring
# print(spt.Portfolio.__doc__)

# Retrieving the docstring of the Portfolio class functions of your choosing
# print(spt.Portfolio.add_record.__doc__)

# Testing the functionality
#   1. Create 2 objects of the Portfolio class and test key functionality of the .

#print(help(spt.Portfolio))
client1 = {'fname': 'Rogers',
           'lname' : 'Kiome',
           'holdings' : ['Safaricom', 'KCB', 'Tesla'],
           'transactions' : 25000}
portfolio1 = spt.Portfolio(client1)
print(portfolio1.client)
#
#  2. Indentify possible functionality bugs that may occur and note them down. Will handle this in details in
#       error handling and testing topics
#       (i).    Logical error: no control over cleint details passed through
#       (ii).   

