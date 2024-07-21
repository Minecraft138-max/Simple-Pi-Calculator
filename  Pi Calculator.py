# Created on iPad.

import math

number = 0.00000000001
a = (math.sin (number * math.pi/180))**2
b = (1-math.cos (number * math.pi/180))**2
c = 180 * math.sqrt (a + b)/number
print (c)