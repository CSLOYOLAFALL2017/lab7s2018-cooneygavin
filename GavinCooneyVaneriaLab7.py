# Grace Cooney, Nick Gavin, Michael Vanaria
# Course CS151.01
# Date: March 21, 2018
# Lab Number 7
# Problem Statement: You've been hired to study the movie industry and how much money various movies have made over the past few decades.
# Data in: Inputs
# Data out: File name, max profit,
# Other files needed: movies.csv
# Credits: N/A

#This program will output the movie with the highest profit and will save all the info on all movies to a new file


#Function's purpose: read in a file name from the user and return it once they give one that exists

import os

def fileName():
    fileInput=input("What file would you like to read?")
    while not os.path.exists(fileInput):
        fileInput=input("What file would you like to read?")
    return fileInput

# Function's purpose: Determine the maximum profit
def profit():
    profit_file = open("movies.csv", "r")
    profitMade = 0
    for line in profit_file:
        date, title, budget, gross = line.split(",")
        budget=float(budget)
        gross=float(gross)
        movieProfit = gross - budget
        if movieProfit > profitMade:
            profitMade = movieProfit
            return profitMade

# Function's purpose: Save info on all movies to a new file
def newFile():
    old_file = open("movies.csv", "r")
    userinput = input("What do you want to name the new file?")
    new_file = open(userinput, "w")
    for line in old_file:
        date, title, budget, gross= line.split(",")
        budget = float(budget)
        gross= float(gross)
        print(date, title, budget, gross, file=new_file)

    new_file.close()


# Function purpose: Main function
def main():
    file = fileName()
    highestProfit= profit()
    saveNew= newFile()
    print("The file name is", file)
    print("The highest movie profit was $", highestProfit, sep = "")
    print("Your new file has been saved to a new file")

main( )

