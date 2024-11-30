# Exercise: Hash Table: New York City Weather Analysis
# (1) nyc_weather.csv contains new york city weather for first few days in the month of January. Write a program that can answer following,

#   (a) What was the average temperature in first week of Jan

#   (b) What was the maximum temperature in first 10 days of Jan

#   Figure out data structure that is best for this problem



dict=[]
with open('nyc_weather.csv','r') as f:
    for line in f:
        tokens=line.split(',')
        key=tokens[0]
        value=tokens[1]
        dict.append((key,value))

sum=0
for i,element in enumerate(dict):
    if i>6:
        break
    sum += int(element[1])
average=sum/7


max=dict[0][1]
for i in range(len(dict)):
    if dict[i][1]>max:
        max=dict[i][1]

print(max)

weather_dict = {}

with open("nyc_weather.csv","r") as f:
    for line in f:
        tokens = line.split(',')
        day = tokens[0]
        try:
            temperature = int(tokens[1])
            weather_dict[day] = temperature
        except:
            print("Invalid temperature.Ignore the row")
weather_dict['jan 9']