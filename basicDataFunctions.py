import csv
import math

def getData(fileToOpen):
	rowsOfData = None
	with open(fileToOpen) as f:
		reader = csv.DictReader(f)
		rowsOfData = list(reader)
	return rowsOfData

def getBasicDataInfo(fileName):
	with open(fileName) as f:
		reader = csv.DictReader(f)
		print "\n\nThere are %r fields in this dataset. " % len(reader.fieldnames) 
		print " -----------------------------------------------------------------"
		return (reader.fieldnames) 

def chooseToConvertString(fileName, fieldList):
	rowsOfData = getData(fileName)

	for field in fieldList:
		for dataRow in rowsOfData:
			dataRow[field] = int(dataRow[field])
	return rowsOfData	

def getMaxMin(rowsOfData, fieldNames):
	maxMinTupleList = []
	for field in fieldNames:
		maxMinList = []
		for dataRow in rowsOfData:
			maxMinList.append(int(dataRow[field]))
		maxMinTupleList.append((min(maxMinList),max(maxMinList)))
	return maxMinTupleList

def getAvg (rowsOfData, fieldName):
	sum = 0
	for dataRow in rowsOfData:
		sum+= dataRow[fieldName]
	return sum/len(rowsOfData)


def getVariance(rowsOfData, fieldName):
	sumOfSubtractionsSquared = 0
	avg = getAvg(rowsOfData, fieldName)
	for dataRow in rowsOfData:
		sumOfSubtractionsSquared = sumOfSubtractionsSquared + ((dataRow[fieldName] - avg)**2)
	return (sumOfSubtractionsSquared/len(rowsOfData))

def getStandardDeviation(rowsOfData, fieldName):
	variance = getVariance(rowsOfData, fieldName)
	return math.sqrt(variance)



def getAvg (rowsOfData, fieldName):
	sum = 0
	for dataRow in rowsOfData:
		sum+= dataRow[fieldName]
	# print len(admissionDecisionRows)
	return sum/len(rowsOfData)
