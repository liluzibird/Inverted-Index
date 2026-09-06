#-------------------------------------------------------------------------
# AUTHOR: Albert Huynh
# FILENAME: invertedIndex.py
# SPECIFICATION: Build inverted index for document collection with surface-level normalization and lemmatization to generate the index terms.
# FOR: CS 4250 - Assignment #1
# TIME SPENT: 5 hours
#-------------------------------------------------------------------------

# Importing Python libraries
import pandas as pd
import re

# Reading the document collection
data = pd.read_csv("Assignment 1/collection.csv")



# Defining the dictionary used for lemmatization
# --> add your Python code here
lemmas = {
    "homes":"home", "increases":"increase", "increasing":"increase", "sales":"sale", "rising":"rise", "homes":"home"
}

# Creating the data structure that will store the inverted index
invertedIndex = {}

# Processing each document in the collection
for i, row in data.iterrows():

    docID = row["Document"]
    text = row["Text"]

    # Applying surface-level normalization
    # --> add your Python code here
    text = text.lower()


    # Tokenizing the document
    # --> add your Python code here
    tokens = re.findall(r'\b[a-z]+\b', text) #use regex to tokenize


    # Applying lemmatization
    # --> add your Python code here
    lemmatized_tokens = [lemmas.get(token, token) for token in tokens]
    


    # Building the inverted index
    # --> add your Python code here
    for term in lemmatized_tokens:
        if term not in invertedIndex:
            invertedIndex[term] = []
        if docID not in invertedIndex[term]:
            invertedIndex[term].append(docID)


# Printing the inverted index with terms ordered alphabetically
# Expected format:
# term1 : ['Doc1', 'Doc2']
# term2 : ['Doc3']
# --> add your Python code here
for term in sorted(invertedIndex.keys()):
    print(f"{term} : {invertedIndex[term]}")