while True:
    name = (input("\nEnter a stock symbol: ")).upper();lineData = open("task5.csv","r").read().split("\n");newData = [];stocks = []
    for i in lineData:newData.append(i.split(","))
    stocks = [i for i in newData if name in i[0]]
    print("No matches") if len(stocks) == 0 else print(f"There are {len(stocks)} stocks with that symbol")
    if len(stocks) == 1:print((stocks[0][1]).replace('"', ""))