import numpy as np
import math
X_LIMIT = 7
Y_LIMIT = math.sqrt(33)

def on_elipse(x,y):
	function_value = (x**2)/49 + (y**2)/33
	if 0.9999 < function_value and function_value < 1.0001:
		return True
	else:
		return False
		
def on_circle(x,y):
	function_value = x**2 + (y-3)**2
	if 3.9999 < function_value and function_value < 4.0001:
		return True
	else:
		return False

# Setting domain and target set
domain = np.linspace(-X_LIMIT,X_LIMIT,10000,endpoint=True)
target_set = np.linspace(-Y_LIMIT,Y_LIMIT,10000,endpoint=True)

elipse_point = []
circle_point = []

# rounding coordinate system
for xx in domain:
	for yy in target_set:
		if on_elipse(xx,yy):
			elipse_point.append((xx,yy))
		if on_circle(xx,yy):
			circle_point.append((xx,yy))

# Recording elipse
with open("elipse.txt","w") as f:
	result = ""
	for point in elipse_point:
		result += str(point[0]) + " " + str(point[1]) + "\n"
	f.write(result)
	
# Recording circle
with open("circle.txt","w") as f:
	result = ""
	for point in circle_point:
		result += str(point[0]) + " " + str(point[1]) + "\n"
	f.write(result)
	