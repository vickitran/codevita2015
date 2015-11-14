from __future__ import division

# desired cash flow - M
# period in months - T
# rate per annum - R
lines = []

for i in range(0,3):
	lines.append(input())

M = float(lines[0])
T = float(lines[1])
R = float(lines[2])

# We recognize the problem as level payment annuity.
if R == 0:
	present_value = M*T
else:
	R = (R/12/100)
	Rp = 1+R
	Radj = Rp**(-T)
	present_value = M*(1-Radj)/R

print(int(round(present_value,0)))