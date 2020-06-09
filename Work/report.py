# report.py
#
# Exercise 2.4
import csv

def read_portfolio(filename):
    """Carica il contenuto del file in una lista di tuple"""

    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        header = next(f)
        for row in rows:
            holding = (row[0], row[1], row[2])
            portfolio.append(holding)
    return portfolio







print(read_portfolio("Data/portfolio.csv"))