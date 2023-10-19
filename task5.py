"""
Read the data from the file task02.csv
Allow the user to search for a stock symbol.
If the stock symbol is found, display the name of the company
If a multiple stocks match the symbol, say there are multiple stocks available
If there is no match, say "no match found"

Example:
Enter stock symbol: AA
There are 21 stocks with that symbol
Enter stock symbol: AAPL
Apple Inc.
Enter stock symbol: YANG
No matches
"""


def find():
    name = (input("\nEnter a stock symbol: ")).upper()
    lineData = open("task5.csv","r").read().split("\n")
    newData = []
    stocks = []
    number = 0
    for i in lineData:
        x = i.split(",")
        newData.append(x)
    for i in newData:
        if name in i[0]:
            number +=1
            stocks.append(i)
    if number == 1:print((stocks[0][1]).replace('"', ""))
    else: print(f"There are {number} stocks with that symbol")

while True:
    find()