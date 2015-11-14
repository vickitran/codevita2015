map = []

current_input = ""

while(current_input != "-1"):
	current_input = input()
	minimap = [element for element in current_input.replace(" ", "")]
	map.append(minimap)

row = int(map[0][0])
columns = int(map[0][1])

ycoordbase = ""
xcoordbase = ""
explorers_location = []

for list in map:
	try:
		ycoordbase = list.index('d')
		xcoordbase = map.index(list.index('d'))
		explorers_location.append(map.index(list.index('s')),list.index('s'))
	except:
		continue

print(xcoordbase,ycoordbase)