import numpy as np
import csv as csv
import scipy as sp
import pandas as p
import matplotlib as mpl

# Open up the csv file in to a Python object
csv_file_object = csv.reader(open('../data/train.csv', 'rb'))
# The next() command just skips the  first line which is a header
header = csv_file_object.next()

data=[]                          # Create a variable called 'data'.
for row in csv_file_object:      # Run through each row in the csv file,
    data.append(row)             # adding each row to the data variable

data = np.array(data)

# The size() function counts how many elements are in
# in the array and sum() (as you would expects) sums up
# the elements in the array.

number_passengers = np.size(data[0::,1].astype(np.float))
number_survived = np.sum(data[0::,1].astype(np.float))
proportion_survivors = number_survived / number_passengers

women_only_stats = data[0::,4] == "female" # This finds where all
# the elements in the gender
# column that equals female
men_only_stats = data[0::,4] != "female"   # This finds where all the
# elements do not equal
# female (i.e. male)

# Using the index from above we select the females and males separately
women_onboard = data[women_only_stats,1].astype(np.float)
men_onboard = data[men_only_stats,1].astype(np.float)

# Then we finds the proportions of them that survived
proportion_women_survived = np.sum(women_onboard) / np.size(women_onboard)
proportion_men_survived = np.sum(men_onboard) / np.size(men_onboard)

# and then print it out
print 'Proportion of women who survived is %s' % proportion_women_survived
print 'Proportion of men who survived is %s' % proportion_men_survived