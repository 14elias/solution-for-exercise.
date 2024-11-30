# poem.txt Contains famous poem "Road not taken" by poet Robert Frost. 
# You have to read this file in python and print every word and its count as show below. 
# Think about the best data structure that you can use to solve this problem 
# and figure out why you selected that specific data structure.

#  'diverged': 2,
#  'in': 3,
#  'I': 8
dict = {}
count=1
with open("poem.txt","r") as f:
    for line in f:
        tokens = line.split(' ')
        for token in tokens:
            token=token.replace('\n','')
            if token in dict:
                dict[token] +=1
            else:
                dict[token]=1
