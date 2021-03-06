documents = (
"The sky is blue",
"The sun is bright",
"The sun in the sky is bright",
"We can see the shining sun, the bright sun"
)

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import math


#transform documents into the TF-IDF matrix:
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(documents)
print tfidf_matrix.shape
(4, 11)

#calculate the Cosine Similarity between the first document
#with each of the other documents of the set:

cos_sim = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix)
#array = [ 1.        ,  0.36651513,  0.52305744,  0.13448867]

#check the angle between the first and third documents:
# This was already calculated on the previous step, so we just use the value
cos_sim = 0.52305744
angle_in_radians = math.acos(cos_sim)
print math.degrees(angle_in_radians)
