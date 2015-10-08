import numpy as np
import csv as csv
import scipy as sp
import pandas as p
import matplotlib as mpl

test_file = open('../data/test.csv', 'rb')
test_file_object = csv.reader(test_file)
header = test_file_object.next()

prediction_file = open("../data/output/genderbasedmodel.csv", "wb")
prediction_file_object = csv.writer(prediction_file)

prediction_file_object.writerow(["PassengerId", "Survived"])
for row in test_file_object:       # For each row in test.csv
    if row[3] == 'female':         # is it a female, if yes then
        prediction_file_object.writerow([row[0],'1'])    # predict 1
    else:                              # or else if male,
        prediction_file_object.writerow([row[0],'0'])    # predict 0
test_file.close()
prediction_file.close()