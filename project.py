# project.py
# a program to predict a baseball players future performance and how much they should be paid
import numpy as np
import pandas as pd
from pybaseball import batting_stats 
import pdb


def main():
    # get the data out of pybaseball
    data = batting_stats(2020,2021)
    x = np.array(data)
    columns = data.columns.tolist()
    col = ['Name', 'Age', 'RBI']

    stats = []
    for name in col:
        ind = columns.index(name)
        stats.append(x[:, ind])
    stats = np.array(stats).transpose()

    pdb.set_trace()
    
    # ask user for a players name to pull up the statistics

    # predict how much a player should make



if __name__ == "__main__":
    main()