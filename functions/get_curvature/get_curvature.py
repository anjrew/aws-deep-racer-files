import math
import numpy as np


# Gets the average curvature of the road ahead based on the agents position and the given waypoints that are ahead of the agent.
# def get_curvature(agent_pos: tuple[int,int], ahead_waypoints: list[tuple[int,int]]):
    # amount_of_waypoints = len(ahead_waypoints)
    # if amount_of_waypoints < 2:
    #     raise Exception(f'There must be at least 2 waypoints given to calculate curvature. Only {amount_of_waypoints} were given')

a = (3,6)
b = (3,4)
c = (5,2)


def test():
    p1 = a
    p2 = c

    # Difference in x coordinates
    dx = p2[0] - p1[0]

    # Difference in y coordinates
    dy = p2[1] - p1[1]

    # Angle between p1 and p2 in radians
    theta = math.atan2(dy, dx)

    return theta

result = test()

print(result)

 
def getAngle(a, b, c):
    ang = math.degrees(math.atan2(c[1]-b[1], c[0]-b[0]) - math.atan2(a[1]-b[1], a[0]-b[0]))
    return ang + 360 if ang < 0 else ang
 
print(getAngle(a, b, c))

print(math.degrees(math.atan2(a[1] - b[1], a[0] - b[0])))
print(math.degrees(math.atan2(a[1] - c[1], a[0] - c[0])))
print(math.degrees(math.atan2(b[1] - c[1], b[0] - c[0])))
print(math.degrees(math.atan2(c[1] - b[1], c[0] - b[0])))
print(math.degrees(math.atan2(c[1] - a[1], c[0] - a[0])))
print(math.degrees(math.atan2(b[1] - a[1], b[0] - a[0])))
print(math.degrees(math.atan2(c[1] - b[1], c[0] - b[0])))



import numpy as np
points = np.array([[343.8998, 168.1526], [351.2377, 173.7503], [353.531, 182.72]])

print('points2 is',points[2])
A = points[2] - points[0]
B = points[1] - points[0]
C = points[2] - points[1]
print('a is', A)

angles = []
for e1, e2 in ((A, B), (A, C), (B, -C)):
    num = np.dot(e1, e2)
    denom = np.linalg.norm(e1) * np.linalg.norm(e2)
    angles.append(np.arccos(num/denom) * 180 / np.pi)
print(angles)
print(sum(angles))

# Python3 code to find all three angles
# of a triangle given coordinate
# of all three vertices
import math

# returns square of distance b/w two points
def lengthSquare(X, Y):
	xDiff = X[0] - Y[0]
	yDiff = X[1] - Y[1]
	return xDiff * xDiff + yDiff * yDiff
	
def printAngle(A, B, C):
	
	# Square of lengths be a2, b2, c2
	a2 = lengthSquare(B, C)
	b2 = lengthSquare(A, C)
	c2 = lengthSquare(A, B)

	# length of sides be a, b, c
	a = math.sqrt(a2);
	b = math.sqrt(b2);
	c = math.sqrt(c2);

	# From Cosine law
	alpha = math.acos((b2 + c2 - a2) /
						(2 * b * c));
	betta = math.acos((a2 + c2 - b2) /
						(2 * a * c));
	gamma = math.acos((a2 + b2 - c2) /
						(2 * a * b));

	# Converting to degree
	alpha = alpha * 180 / math.pi;
	betta = betta * 180 / math.pi;
	gamma = gamma * 180 / math.pi;

	# printing all the angles
	print("alpha : %f" %(alpha))
	print("betta : %f" %(betta))
	print("gamma : %f" %(gamma))
		

printAngle(a, b, c);

# This code is contributed
# by ApurvaRaj
