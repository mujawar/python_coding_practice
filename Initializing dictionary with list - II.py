#We want to make a dictionary with the number of digits as the key and list of numbers the value:
from collections import defaultdict
L = [1,2,4,8,16,32,64,128,256,512,1024,32768,65536,4294967296]

d = defaultdict(list)
print(d)
for i in L:
    print("d[len(str(i))]",d[len(str(i))],i)
    d[len(str(i))].append(i)

print(d)
