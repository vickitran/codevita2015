import math

testCase = []
columnGroup = []
columnAgg = []
currentInput = ""
duplicates = []
'''
Sum
Average
Invert
Count
'''
while (currentInput != "-1"):
# loop, until -l entered
	currentInput = input()
	testCase.append(currentInput)

function = testCase[0]
groupingColNum = int(testCase[1])
aggregateColNum = int(testCase[2])


row = 0
startData = 2
while row < len(testCase) - 4:
	startData += 1
	allData = testCase[startData].split()
	columnGroup.append(allData[groupingColNum-1])
	columnAgg.append(allData[aggregateColNum-1])
	row += 1

dataTuple = list(zip(columnGroup, columnAgg))
sortedTuple = sorted(dataTuple, key = lambda e: e[0])

def summation():
	numberData = []
	for number in columnAgg:
		numberData.append(float(number))

	dataTuple = list(zip(columnGroup, numberData))
	sortedTuple = sorted(dataTuple, key = lambda e: e[0])
	count = 0
	counterIndex = 0
	currentSum = 0
	for data in sortedTuple:
		if count >= 1:
			if data[0] == sortedTuple[counterIndex-1][0]:
				if data[0] not in duplicates:
					duplicates.append(data[0])
		count += 1
		counterIndex += 1

	counterIndex = 0
	noDuplicates = list(set(sortedTuple))
	for data in noDuplicates:
		for duplicate in duplicates:
			if data[0][0] == duplicate:
				noDuplicates[counterIndex] = (data[0], sum(x[1] for x in sortedTuple if x[0] == duplicate))
	counterIndex += 1
	noDuplicates.sort()
	for data in noDuplicates:
		print (str(data[0]) + " " + str(math.ceil(data[1])))
	# remove duplicates
	# modify new summation

if function == "Sum":
	summation()


