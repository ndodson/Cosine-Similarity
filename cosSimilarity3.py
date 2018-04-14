import re, math
from collections import Counter
import math

WORD = re.compile(r'\w+')


#cosine of 2 vectors function
def get_cosine(vec1, vec2):
     intersection = set(vec1.keys()) & set(vec2.keys())
     numerator = sum([vec1[x] * vec2[x] for x in intersection])

     sum1 = sum([vec1[x]**2 for x in vec1.keys()])
     sum2 = sum([vec2[x]**2 for x in vec2.keys()])
     denominator = math.sqrt(sum1) * math.sqrt(sum2)

     if not denominator:
        return 0.0
     else:
        return float(numerator) / denominator

#text to vector representation
def text_to_vector(text):
     words = WORD.findall(text)
     return Counter(words)

#declare some sentences
text1 = 'This is a foo bar sentence .'
text2 = 'This sentence is similar to a foo bar sentence .'
text3 = 'A string that should not be close to the others!'

#call text to vector
vector1 = text_to_vector(text1)
vector2 = text_to_vector(text2)
vector3 = text_to_vector(text3)


#calculate cosine with vector form inputs
cosine1 = get_cosine(vector1, vector2)
cosine2 = get_cosine(vector1, vector3)


#format the output
angle_in_radians = math.acos(cosine1)
degrees1 = math.degrees(angle_in_radians)

angle_in_radians = math.acos(cosine2)
degrees2 =  math.degrees(angle_in_radians)

#return a similarity percentage estimate
print "String 1 is:   " + text1
print "String 2 is:  " + text2
print "String 3 is:  " + text3
print "the cosine similarity percentage of string 1 and 2 is " + str(degrees1)


print "the cosine similarity percentage of string 1 and 3 is " + str(degrees2)
