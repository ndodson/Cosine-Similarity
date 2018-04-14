import numpy as np
import math



def cos_sim(a, b):
	"""Takes 2 vectors a, b and returns the cosine similarity according
	to the definition of the dot product
	"""
	dot_product = np.dot(a, b)
	norm_a = np.linalg.norm(a)
	norm_b = np.linalg.norm(b)
	return dot_product / (norm_a * norm_b)



sentence_m = "this is my string"
sentence_h = "this is mine too"

# the counts we computed above
sentence_m = np.array([0, 0, 1, 1, 1, 1, 0, 0, 0])
sentence_h = np.array([0, 0, 1, 1, 1, 1, 0, 0, 0])
sentence_w = np.array([0, 0, 0, 1, 0, 0, 1, 1, 1])

# We should expect sentence_m and sentence_h to be more similar
print(cos_sim(sentence_m, sentence_h)) # 0.5
print(cos_sim(sentence_m, sentence_w)) # 0.25

similarity1 = cos_sim(sentence_m, sentence_h)
similarity2 = cos_sim(sentence_m, sentence_w)

angle_in_radians = math.acos(similarity1)
print math.degrees(angle_in_radians)

angle_in_radians = math.acos(similarity2)
print math.degrees(angle_in_radians)
