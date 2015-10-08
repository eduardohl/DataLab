import numpy as numpy
import csv as csv
import scipy as scipy
import pandas as pandas
import matplotlib as matplotlib

train_file = open("../data/train.csv", "rb")
csv_file_object = csv.reader(train_file)
header = csv_file_object.next()
data=[]
for row in csv_file_object:
    data.append(row)
data = numpy.array(data)

fare_ceiling = 40
data[ data[0::,9].astype(numpy.float) >= fare_ceiling, 9 ] = fare_ceiling - 1.0

fare_bracket_size = 10
number_of_price_brackets = fare_ceiling / fare_bracket_size

number_of_gender = len(numpy.unique(data[0::,4]))
number_of_classes = len(numpy.unique(data[0::,2]))

survival_table = numpy.zeros((number_of_gender, number_of_classes, number_of_price_brackets))

print data
for ticket_class in xrange(number_of_classes):
    for price_bracket in xrange(number_of_price_brackets):
        women_stats = data[
            #All conditions given, so produce me a matrix of my data vector, where all these conditions are true
            (data[0::,4] == "female") &
            (data[0::,2].astype(numpy.float) == ticket_class + 1) &
            (data[0::,9].astype(numpy.float) >= price_bracket * fare_bracket_size) &
            (data[0::,9].astype(numpy.float) <  (price_bracket + 1) * fare_bracket_size)
            #And mark if survived or not
            , 1
        ]
        men_stats = data[
            #All conditions given, so produce me a matrix of my data vector, where all these conditions are true
            (data[0::,4] == "male") &
            (data[0::,2].astype(numpy.float) == ticket_class + 1) &
            (data[0::,9].astype(numpy.float) >= price_bracket * fare_bracket_size) &
            (data[0::,9].astype(numpy.float) <  (price_bracket + 1) * fare_bracket_size)
            #And mark if survived or not
            , 1
        ]
        survival_table[0,ticket_class,price_bracket] = numpy.mean(women_stats.astype(numpy.float))
        survival_table[1,ticket_class,price_bracket] = numpy.mean(men_stats.astype(numpy.float))

survival_table[survival_table != survival_table] = 0 # Remove crappy NaN
survival_table[survival_table < 0.5] = 0             # Assume who lived and died
survival_table[survival_table >= 0.5] = 1
print survival_table
train_file.close()

test_file = open("../data/test.csv", "rb")
test_file_obj = csv.reader(test_file)
header = test_file_obj.next()

csv_prediction_file = open("../data/output/py_model.csv", "wb")
csv_prediction_obj = csv.writer(csv_prediction_file)
csv_prediction_obj.writerow(["PassengerId", "Survived"])

for row in test_file_obj:
    for price_bracket in xrange(number_of_price_brackets):
        try:
            row[8] = float(row[8])
        except:
            bin_fare = 3 - float(row[1])
            break
        if row[8] > fare_ceiling:
            bin_fare = number_of_price_brackets - 1
            break
        if row[8] >= price_bracket * fare_bracket_size and row[8] < (price_bracket + 1) * fare_bracket_size:
            bin_fare = price_bracket
            break
    if row[3] == 'female':
        csv_prediction_obj.writerow([row[0], "%d" % int(survival_table[0, float(row[1]) - 1, bin_fare])])
    else:
        csv_prediction_obj.writerow([row[0], "%d" % int(survival_table[1, float(row[1]) - 1, bin_fare])])

test_file.close()
csv_prediction_file.close()




