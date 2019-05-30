import math
import numpy as np
X_LIMIT = 7
Y_LIMIT = math.sqrt(33)

def get_distance(x1,y1,x2,y2):
	return math.sqrt((x2-x1)**2 + (y2-y1)**2)
	
def get_distance(P,Q):
	return math.sqrt((P[0]-Q[0])**2 + (P[1]-Q[1])**2)
	
elipse_point = []
circle_point = []

F = (4,0)
F_prime = (-4,0)

# Loading points of elipse
with open("elipse.txt","r") as f:
	result = f.readlines()
	for line in result:
		data = line.split(' ')
		xx = float(data[0])
		yy = float(data[1])
		elipse_point.append((xx,yy))
		
# Loading points of circle
with open("circle.txt","r") as f:
	result = f.readlines()
	for line in result:
		data = line.split(' ')
		xx = float(data[0])
		yy = float(data[1])
		circle_point.append((xx,yy))
		
# Finding answer
answer = 0
for P in circle_point:
	slope = float(F_prime[1]-P[1])/(F_prime[0]-P[0])
	y_intercept = F_prime[1]-slope*F_prime[0]
	for Q in elipse_point:
		if(Q[1] < 0):
			continue
		result = Q[0]*slope + y_intercept
		
		#if Q is on line F'P
		if result - 0.01 < Q[1] and Q[1] < result + 0.01:
			answer = max((answer,get_distance(P,Q)+get_distance(F,Q)))
			ansP = P
			ansQ = Q
			
print(answer)