from cgi import print_directory
from importlib_metadata import functools

#Minimized Difference Sum


tempsort = [1,3,3,2,4,7]
# tempsort  = sorted(arr)
# print(tempsort)
sumarray = []
count = 0
lenArr = len(tempsort) - 1
print(lenArr)
for x in range(len(tempsort)):
    tempabs = abs(tempsort[x]-tempsort[x+1])
    sumarray.append(tempabs)
    count  += 1
    if count == lenArr:
        break

print(sumarray)
FinalResult = functools.reduce(lambda x,y:x+y,sumarray)
print("Final",FinalResult)

