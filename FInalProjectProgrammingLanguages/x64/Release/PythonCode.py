from fileinput import filename
import re
import string
from tkinter import W


def printsomething():
    print("Hello from python!")

def PrintMe(v):
    print("You sent me: " + v)
    return 100;

def SquareValue(v):
    return v * v


#reads the file and saves the data to a dictionary, This will be called by other functions that use the input file
#lines are stripped to prevent line skipping
def ReadFile():
    itemDict = {}
    with open('InputFile.txt') as f:
        lines = f.readlines()
    for line in lines:
        if line.strip() in itemDict:
            itemDict[line.strip()] += 1
        else:
            itemDict[line.strip()] = 1

    return itemDict;


#taking the dictionary and loops through it's keys to print a list.
def CountList():
    itemDict = ReadFile()

    for item in itemDict:
        print(item.strip(), itemDict[item])

#using the dictionary it just returns the number for the requested item, c++ code prints to console
def CheckForItem(item):

    if itemDict.has_key(item):
        itemDict = ReadFile()
        return itemDict[item]
    else:
        return 0


#Using the dictionary it loops theough each key and writes to the frequency.dat file 
def WriteHistogramFile():
    itemDict = ReadFile()
    Histogram_File = open("frequency.dat", W)

    for item in itemDict:
        stars = ""

        #this loops through the amount of an item and creates as many stars as there are of the item
        for i in range(itemDict[item]):
            stars += '*'

        #prints name of item with the stars next to it equal to the amount of the item there is
        Histogram_File.write(item + " " + stars + "\n")
        

    
