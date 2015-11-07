# store entered sums into a list
sums = []
permutations = []
currentInput = ""
# assume max 31, 28, 30 days in month
days31 = list(range(1, 32))
days30 = list(range(1, 31))
days28 = list(range(1, 29))
# add 4 extra days to account for next month
days31.extend(list(range(1,5)))
days30.extend(list(range(1,5)))
days28.extend(list(range(1,5)))
testSum = 0

while (currentInput != "-1"):
# loop, until -l entered
	currentInput = input()
	try:
		sums.append(int(currentInput))
	except:
		sums.append(currentInput)
		continue

# check sums determine combinations and print out
def sumCheck(inputSum):
	# counter to determine every 5 days
	counter = 0
	currentIndex = 0
	valid = 0
	for day in days30:
		counter +=1
		if counter >= 5: # sum the previous 5 days and compare with the input sum
			testSum = days30[currentIndex] + days30[currentIndex-1] + days30[currentIndex-2] + days30[currentIndex-3] + days30[currentIndex-4] 
			testNumbers = str(days30[currentIndex-4]) + " " + str(days30[currentIndex-3]) + " " + str(days30[currentIndex-2]) + " " + str(days30[currentIndex-1]) + " " + str(days30[currentIndex])
			if inputSum == testSum:
				permutations.append(testNumbers)
				valid = 1
		currentIndex += 1
	currentIndex = currentIndex - 3 
	while (currentIndex < 35):
		testSum2 = days31[currentIndex] + days31[currentIndex-1] + days31[currentIndex-2] + days31[currentIndex-3] + days31[currentIndex-4] 
		testNumbers2 = str(days31[currentIndex-4]) + " " + str(days31[currentIndex-3]) + " " + str(days31[currentIndex-2]) + " " + str(days31[currentIndex-1]) + " " + str(days31[currentIndex])
		if inputSum == testSum2:
			permutations.append(testNumbers2)
			valid = 1
		currentIndex += 1
	currentIndex = currentIndex - 9
	while (currentIndex < 32):
		testSum2 = days28[currentIndex] + days28[currentIndex-1] + days28[currentIndex-2] + days28[currentIndex-3] + days28[currentIndex-4] 
		testNumbers2 = str(days28[currentIndex-4]) + " " + str(days28[currentIndex-3]) + " " + str(days28[currentIndex-2]) + " " + str(days28[currentIndex-1]) + " " + str(days28[currentIndex])
		if inputSum == testSum2:
			permutations.append(testNumbers2)
			valid = 1
		currentIndex += 1
	if valid == 0:
		permutations.append("Invalid input")

# ensures ordering of outputs, use sumCheck function on each input
for inputSum in sums:
	if inputSum != -1:
		sumCheck(inputSum)

# print out the results
for permutation in permutations:
	print (permutation)