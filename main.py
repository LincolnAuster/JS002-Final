import bpy
import math

def distance(obj1, obj2):
	l1 = obj1.location
	l2 = obj2.location

	return math.sqrt( (l1[0] - l2[0])**2 + (l1[1] - l2[1])**2 + (l1[2] - l2[2])**2)

def inv_square(distance, intensity):
	return (1/(distance**2)) * intensity

positive = []
positive_d = []
negative = []
negative_d = []

for obj in bpy.context.scene.objects:
	if "Positive" in obj.name:
		positive.append(obj)
	elif "Negative" in obj.name:
		negative.append(obj)

# initialize negative_d and positive_d to zeros
for n in negative:
	negative_d.append(0)
for p in positive:
	positive_d.append(0)

# algorithm: check how far everything is, and record how much everything needs to move
for obj in positive:
	for neg_index in range(len(negative)):
		neg = negative[neg_index]
		d = distance(obj, neg)
		# at 1 meter, it should move 1 unit, so it should move 1/distance^2 units to keep with inverse square law
		# the intensity should be the weight of obj, as obj is acting on neg
		negative_d[neg_index] += inv_square(d, obj["weight"])
	for pos_index in range(len(positive)):
		pos = positive[pos_index]
		d = distance(obj, pos)
		
		if d != 0:
			positive_d[pos_index] += inv_square(d, obj["weight"]) # weight is -1, no need for -= or * -1

for obj in negative:
	for pos_index in range(len(positive)):
		pos = positive[pos_index]
		d = distance(obj, pos)
		positive_d[pos_index] += (inv_square(d, obj["weight"]))
	for neg_index in range(len(negative)):
		neg = negative[neg_index]
		d = distance(obj, neg)
		
		if d != 0:
			negative_d[neg_index] += inv_square(d, obj["weight"]) # weight is -1, no need for -= or * -1

# move everything according to numbers found above
print("Negative: " + str(negative_d))
print(positive_d)
