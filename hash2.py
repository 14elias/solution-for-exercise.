# nyc_weather.csv contains new york city weather for first few days in the month of January. Write a program that can answer following,
# What was the temperature on Jan 9?
# What was the temperature on Jan 4?
# Figure out data structure that is best for this problem
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

print(dict)
            