import math

lines = []

for i in range(0,2):
	lines.append(input())

try:
	a = round(float(lines[0]))
	d = round(float(lines[1]))
	x = round(a - (d/math.sqrt(3)),11)
	y = math.sqrt((a-x)**2+d**2)
	if a > 57*d or d > 1.7*a or a<=0 or d<=0:
		print('Invalid Input')
	else:
		print("X=",'{:.11f}'.format(x),end = '\n')
		print("Y=",'{:.11f}'.format(y))
except ValueError:
	print('Invalid Input')
