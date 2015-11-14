from __future__ import division
from decimal import Decimal
import math

n = float(input())
# if n exceeds 366 people, then probability of someone having the same start date is 100%
if n >= 366:
	print(100.00)
else:	
	fact1 = Decimal(math.factorial(365))
	fact2 = Decimal(math.factorial(365-n))
	prob_complement = fact1/(Decimal(365**n)*fact2)
	print(round((1-prob_complement)*100,2))