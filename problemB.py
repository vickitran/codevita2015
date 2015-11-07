# store entered sums into a list
sums = []
permutations = []
currentInput = ""
# assume max 30 days in month
days = list(range(1, 31))
# add 4 extra days to account for next month
days.extend(list(range(1,5)))
testSum = 0

while (currentInput != "-1"):
# loop, until -l entered
	currentInput = input()
	sums.append(int(currentInput))

# check sums determine combinations and print out
def sumCheck(inputSum):
	# counter to determine every 5 days
	counter = 0
	currentIndex = 0
	for day in days:
		counter +=1
		if counter >= 5: # sum the previous 5 days and compare with the input sum
			testSum = days[currentIndex] + days[currentIndex-1] + days[currentIndex-2] + days[currentIndex-3] + days[currentIndex-4] 
			testNumbers = str(days[currentIndex-4]) + " " + str(days[currentIndex-3]) + " " + str(days[currentIndex-2]) + " " + str(days[currentIndex-1]) + " " + str(days[currentIndex])
			if inputSum == testSum:
				permutations.append(testNumbers)
		currentIndex += 1

# ensures ordering of outputs, use sumCheck function on each input
for inputSum in sums:
	sumCheck(inputSum)

# print out the results
for permutation in permutations:
	print (permutation)