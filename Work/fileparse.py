# fileparse.py
#
# Exercise 3.3

import csv


def parse_csv(filename, types=None):
    """
    Parsifico il file csv passato dentro un dictionary
    """
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)  # Intestazioni colonne
        # if select:
        #     indices = [headers.index(colname) for colname in select]
        # else:
        #     indices = []

        records = []
        for row in rows:
            if not row:   # Se non contiene date
                continue

            if types:
                row = [func(val) for func, val in zip(types, row)]
            # Make a dictionary
            record = dict((zip(headers, row)))
            records.append(record)

    return records

select = ['name', 'shares']
portfolio = parse_csv('Data/portfolio.csv', types=[str, int, float])
print(portfolio)
