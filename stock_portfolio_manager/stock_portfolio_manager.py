"""
Program:
---------------------------
stock portfolio manager.

usage:
---------------------------
Maintains a record of shareholders holdings in various companies.

Author:
---------------------------
Kelvin Macharia
Rogers Kiome
Caroline Ayieko

"""

import datetime
import pprint
from typing import Dict, List, Any

COMPANIES = [
    {"name": "Safaricom Plc", "initials": "SCOM:NAI"},
    {"name": "Centum Investment Company PLC", "initials": "CTUM:NAI"},
    {"name": "NCBA Group PLC", "initials": "NCBA:NAI"}
]

CLIENTS = [
    {"first_name": "Caroline", "last_name": "Ayieko"},
    {"first_name": "Rogers", "last_name": "Kiome"},
    {"first_name": "Kelvin", "last_name": "Macharia"}
]


class Portfolio:
    """
    Portfolio class.
    Manage clients stock portfolio.
    Instance of this class represents a client.
    The instance contains the clients details, holdings and record of past transaction
    """

    def __init__(self, client_details: Dict[str, Any]):
        self.client = client_details
        self.holdings: Dict[str, int] = {}  # key = company, value = number of shares
        self.records: List[Dict[str, Any]] = []  # each record is a dictionary appended to this list

    @staticmethod
    def add_record(transaction_type: str, company: str, shares: int) -> Dict[str, Any]:
        """
        Format a record.
        This function is reusable for both selling and buying transactions.
        :param transaction_type: str - Type of transaction ('buying' or 'selling')
        :param company: str - Name of the company
        :param shares: int - Number of shares
        :return: dict - Formatted transaction record
        """
        current_date = datetime.datetime.now()
        current_date_format = current_date.strftime("%H:%M:%S")
        transaction_record = {
            "date": current_date_format,
            "transaction_type": transaction_type,
            "company": company,
            "quantity": shares
        }
        return transaction_record

    def buy(self, company: str, shares: int):
        """
        Execute a buying transaction.
        Call add_record to format the transaction and append it to records.
        :param company: str - Name of the company
        :param shares: int - Number of shares to buy
        """
        # buy the stock
        self.holdings[company] = self.holdings.get(company, 0) + shares

        # record transaction
        record = self.add_record("buying", company, shares)
        self.records.append(record)

    def sell(self, company: str, shares: int):
        """
        Execute a selling transaction.
        Call add_record to format the transaction and append it to records.
        :param company:
        :param shares:
        :return:
        """
        # sell the stock
        self.holdings[company] = self.holdings.get(company, 0) - shares

        # record the transaction
        record = self.add_record("selling", company, shares)
        self.records.append(record)

    def __iter__(self):
        """
        Make the holdings iterable to allow looping through.
        :return: iterator - An iterator over the holdings items
        """
        return iter(self.holdings.items())


# self test code
if __name__ == "__main__":
    # Create a portfolio for a test client
    portfolio = Portfolio(CLIENTS[0])

    # Buy some shares
    portfolio.buy(COMPANIES[0]['name'], 50)
    portfolio.buy(COMPANIES[1]['name'], 30)

    # Sell some shares
    portfolio.sell(COMPANIES[0]['name'], 100)

    # Print the portfolio holdings
    pprint.pprint(portfolio.holdings)

    # Print the transaction records
    pprint.pprint(portfolio.records)


# Structure of the program
# logging especially for transactions and include in the final program after bundling for inspection
# Unittest
# Database integration
# Remove hardcoded data
# make this a package
# Packaging with pyinstaller as a CLI
