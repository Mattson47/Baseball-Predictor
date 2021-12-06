# project.py
# a program to predict a baseball players future performance and how much they should be paid
import numpy as np
import pandas as pd
from pybaseball import batting_stats 

def main():
    # get the data out of pybaseball
    data = batting_stats(2010,2021)
    RBI = data('Name','Age','Rbi')
    outfile = open("RBI.txt")
    print(RBI)
    
    # ask user for a players name to pull up the statistics

    # predict how much a player should make



if __name__ == "__main__":
    main()