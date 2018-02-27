import re
from collections import Counter

def clean_and_count(sent, stops):
	"""Takes a string and removes all punctuation and stop words, then returns the frequency table in a Counter obj"""
    cleaned = [re.sub("\W","",x) for x in sent.split(" ") if x not in stops]
    return Counter(cleaned)
