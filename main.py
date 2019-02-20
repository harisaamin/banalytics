
from sys import argv
import basicDataFunctions as bdf
import matplotlib.pyplot as plt


script, fileName = argv
rowsOfData = bdf.getData(fileName)

choice = None

# def dataWranglingMenu():
	

# 	return {
#         1: getMaxMin(,
#         2: 2
#     }.get(x, 9)   

while (choice != "exit"):

	print "\n\nHere is some basic information regarding the data set.\n"
	print bdf.getBasicDataInfo(fileName)
	print """Following are further options:\n 
	1 - Convert To Integer:- Provide Field Name in the form Field1, Field2, .. FieldN to convert relevant fields to Integer Values\n 
	2 - Get Maximum and Minimum:- Provide Field Name in the form "fieldName" Of an Integer Field to get its maximum and minimum value\n 
	3 -  Get Avg:- Provide Field Name for Average Score, in the form 'Field1'."""

	choice = raw_input("What do you waant to do?\n\n>> ")
	choiceList = choice.split(", ")
	if len(choiceList) > 1:
		if int(choiceList[0]) == 1:
			rowsOfData = bdf.chooseToConvertString(fileName, choiceList[1:])
		elif int(choiceList[0]) is 2:
			rowsOfData = bdf.getData(fileName)
			MaxMinTupleList = bdf.getMaxMin(rowsOfData, choiceList[1:])
			print MaxMinTupleList
		elif int(choiceList[0]) is 3:
			print bdf.getAvg(rowsOfData, choiceList[1])
		elif int(choiceList[0]) is 4:
			print bdf.getStandardDeviation(rowsOfData, choiceList[1])
	else:
		break


# def showLinePlot():
# 	TOEFL_SCORES_LIST = []
# 	CHANCE_OF_ADMIT = []
# 	plt.axis([0,1, 20, 120])
# 	for dataRow in rowsOfData:
# 		TOEFL_SCORES_LIST.append(dataRow['TOEFL Score'])
# 		CHANCE_OF_ADMIT.append(dataRow['Chance of Admit '])

# 	plt.scatter(CHANCE_OF_ADMIT, TOEFL_SCORES_LIST)
# 	plt.show()	
