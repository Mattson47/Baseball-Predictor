# project.py
# a program to predict a baseball players future performance and how much they should be paid

# import the packages needed
import numpy as np
import pandas as pd
from pybaseball import batting_stats 
import pdb
from sklearn.linear_model import LinearRegression

def main():
    # get the data out of pybaseball
    data = batting_stats(2018,2019)
    x = np.array(data)
    columns = data.columns.tolist()
    col1 = ['Age', 'H', 'AB', 'HR', 'PA']
    col2 = ['RBI']
    col3 = ['Name']

    # create empty lists for the columns
    stats1 = []
    stats2 = []
    stats3 = []

    # append the values of each predictor variable into a list
    for name in col1:
        ind = columns.index(name)
        stats1.append(x[:, ind])
    
    # append the values for RBI insto a empty list
    for name in col2:
        ind = columns.index(name)
        stats2.append(x[:, ind])

    # create an array of each list
    stats1 = np.array(stats1).transpose()
    stats2 = np.array(stats2).transpose()

    # create a linear regression model
    model = LinearRegression()
    model.fit(stats1, stats2)
    
    # calculate the r squared value
    r_sq = model.score(stats1, stats2)
    print('R-Squared: ', r_sq)
    print('intercept: ', model.intercept_)
    print('slope: ', model.coef_)

    # predict the number of RBI for the following season
    RBI_pred = model.predict(stats1)
    
    for name in col3:
        ind = columns.index(name)
        stats3.append(x[:, ind])
    
    
    
    print(RBI_pred)
    print(stats3)
    
    #print('predicted response: ', RBI_pred, sep = '\n')
    # pdb.set_trace()
    
    # ask user for a players name to pull up the statistics

    # predict how much a player should make

if __name__ == "__main__":
    main()