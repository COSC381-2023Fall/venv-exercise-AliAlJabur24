import requests
from bs4 import BeautifulSoup
import pandas as pd

# take in a url
URL = 'https://www.emich.edu/'

# send a get request and save it in response
response = requests.get(URL)

# Use BeautifulSoup to parse the html response
ParsedData = BeautifulSoup(response.text, 'html.parser')

# go through all the tags in ParsedData and make a list of the tag names
tags = [tag.name for tag in ParsedData.find_all(True)]

# make a panda seris and save it in tag_series
tag_series = pd.Series(tags)

# Count the occurrences of each tag 
tag_counts = tag_series.value_counts()

#loop through the dict and print the tag and the occurrence
for tag, count in tag_counts.items():
    print(str(tag) + ':' + "#" * count)