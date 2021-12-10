# project.py
# a program to predict a baseball players future performance and how much they should be paid


# import the packages needed
import numpy as np
import pandas as pd

# import the batting stats from pybaseball
from pybaseball import batting_stats 
import pdb

# import the linear regression model function from sklearn
from sklearn.linear_model import LinearRegression

def main():
    # get the data out of pybaseball
    # select the date you want the stats to come from
    data = batting_stats(2019,2019)

    # create an array for the data selected
    x = np.array(data)
    columns = data.columns.tolist()

    # create a list for the predictor varaibles
    col1 = ['Age', 'H', 'AB', 'HR']

    # create a list for the predicted variable
    col2 = ['RBI']

    # create a list for the players names
    col3 = ['Name']

    # create an empty list for the predictor variables
    stats1 = []
    # create an empty list for the predicted stats
    predicted_stats = []
    # create an empty list for the batters name
    batters_name = []

    # append the values of each predictor variable into a list
    for name in col1:
        ind = columns.index(name)
        stats1.append(x[:, ind])
    
    # append the values for RBI insto a empty list
    for name in col2:
        ind = columns.index(name)
        predicted_stats.append(x[:, ind])

    # create an array of each list
    stats1 = np.array(stats1).transpose()
    stats2 = np.array(predicted_stats).transpose()

    # create a linear regression model
    model = LinearRegression()
    model.fit(stats1, stats2)
    
    # calculate the r squared value
    r_sq = model.score(stats1, stats2)
    print('R-Squared: ', r_sq)

    # print the intercept of the model and the slope
    print('intercept: ', model.intercept_)
    print('slope: ', model.coef_)

    # predict the number of RBI for the following season
    RBI_pred = model.predict(stats1)
    
    for name in col3:
        ind = columns.index(name)
        batters_name.append(x[:, ind])

    
    # open a file to print the data into
    outfile1 = open('Predicted_RBI.txt', 'w')

    # take the information out of list and print them into a file
    for y in range(len(batters_name[0])):
        a = batters_name[0][y]
        b = RBI_pred[y][0]
        print(a, b, file = outfile1)
        
    
    
    # pdb.set_trace()

    # close the file
    outfile1.close()
    
    # open the file that has the players names and stats
    infile1 = open('Predicted_RBI.txt', 'r')

    # create a new file to write new data into
    outfile2 = open('Name_Change.txt', 'w')
    
    # get rid of any suffix for a player
    for line in infile1:
        name_change = line.split(" ")
        # print the first name, the last name, and the predicted RBI into a new file
        print(name_change[0], name_change[1], name_change[-1], end = '', file = outfile2)
    
    # close the file
    outfile2.close()
    
    # open a file to read
    infile2 = open('Name_Change.txt', 'r')

    # create an empty dictionary
    #data = {}

    # ask user for a players name to pull up the statistics
    players_name = input("Choose a player (capitalize the first letter of each name): ")
    
    # split the players name into their first and last name
    first_name_input, last_name_input = players_name.split(' ')

    for line in infile2:
        #split the line of the infile
        first_name, last_name, RBI_predicted = line.split(" ")
        # make RBI_predicted a float to help calculate the wage
        RBI_predicted = float(RBI_predicted)

        # predict how much a player should make
        # make the base pay $5,000,000
        base_pay = 5000000
        # every RBI that a player is predicted to get is worth an extra $100,000
        RBI_bonus = RBI_predicted * 100000

        # predict the pay by adding the base pay and the RBI_bonus
        predicted_pay = base_pay + RBI_bonus
        if first_name == first_name_input and last_name == last_name_input:
            print(first_name, ' ', last_name, ' ', "is predicted to get", ' ', "{0:0.3f}".format(RBI_predicted), ' ', "RBI next season and he should make $", "{0:0.2f}".format(predicted_pay), ".", sep = "")
            
    
    
    
if __name__ == "__main__":
    main()