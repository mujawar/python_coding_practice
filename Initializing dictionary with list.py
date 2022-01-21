#Initializing dictionary with list - 1
cities = {'San Francisco': 'US', 'London':'UK',
        'Manchester':'UK', 'Paris':'France',
        'Los Angeles':'US', 'Seoul':'Korea'}

# using dict.setdefault(key, default=None)
d2 = {}
for k,v in cities.items():
    # print(k)
    # print(v)
    d2.setdefault(v,[]).append(k)

print(d2)