"""
Program:
---------------------------
stock portfolio manager.

usage:
---------------------------
Maintains a record of shareholders holdings in various companies.
It allows creation and updating of customer portfolio records.

Author:
---------------------------
Kelvin Macharia
Rogers Kiome
Caroline Ayieko

"""

import datetime
import pprint
from typing import Dict, List, Any

# These are a dummy list of companies and clients for testing purposes.
# We would create other classes to onboard customers and companies but for now lets focus on the Portfolio class
#     and utilise this list
companies = [
    {"name": "Safaricom Plc", "initials": "SCOM:NAI", 'available_shares': 5_000_000},
    {"name": "Centum Investment Company PLC", "initials": "CTUM:NAI",  'available_shares': 5_000_000},
    {"name": "NCBA Group PLC", "initials": "NCBA:NAI",  'available_shares': 5_000_000}
]

clients = [
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
        """
        Onboard a client to the stock portfolio manager and initialize their empty portfolio and record of past
        transactions.
        :param client_details: dictionary - client details consisting of first and last names
            Example:
                {"first_name": "Caroline", "last_name": "Ayieko"}
        """
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
        Summary:
            Execute a buying transaction.
        Execution:
            Checks to see how many shares are available for buying
            Calls add_record to format the transaction and append it to records.
        :param company: str - Name of the company
        :param shares: int - Number of shares to buy
        """
        
        # check availability of stock for buying
        for comp in companies:
            if comp['name'] == company and comp['available_shares'] >= shares:
                # if shares are available to buy
                # buy the stock
                self.holdings[company] = self.holdings.get(company, 0) + shares
                # record transaction
                record = self.add_record("buying", company, shares)
                self.records.append(record)
                comp['available_shares'] = comp['available_shares'] - shares
            elif comp['name'] == company and comp['available_shares'] < shares:
                print(f"Available shares are less than {shares:,.2f}")
    def sell(self, company: str, shares: int):
        """
        Summary:
            Execute a selling transaction.
        Execution:
            Call add_record to format the transaction and append it to records.
        :param company: str - company whose shares are being sold
        :param shares: int - amount of shares to sell
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
    p = Portfolio(clients[0])
    print(p.holdings)
    print(p.records)
    print(p.client)
    p.buy("Safaricom Plc",4_000_000)
    p.buy("Safaricom Plc",10_000_001)
    p.buy("Safaricom Plc",5_000_000)
    p.buy("Safaricom Plc",10_000_001)
    print(p.records)
    print(companies[0])

