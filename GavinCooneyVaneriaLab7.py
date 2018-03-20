import os


def fileName():
    fileInput=input("What file would you like to read?")
    while not os.path.exists(fileInput):
        fileInput=input("What file would you like to read?")
    return fileInput


def profit(file):
    profit_file = open(file, "r")
    profitMade = 0
    for line in profit_file:
        date, title, budget, gross = line.split(",")
        budget=float(budget)
        gross=float(gross)
        movieProfit = gross - budget
        if movieProfit > profitMade:
            profitMade = movieProfit
    print("The maximum profit is", profitMade)


def main():
    file = fileName()
    profit(file)


main()