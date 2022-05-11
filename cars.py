

carsArr = [2,12,6,7]
k =3
sortedCars = sorted(carsArr)
print(sortedCars)
min = sortedCars[k-1] - sortedCars[0] +1 
count = 0
lenArr = len(sortedCars) - 1
print("min initail",min)
lenOfArr = len(sortedCars) -1  
print("lenOfArr",lenOfArr)
for i in range(lenOfArr):
    count  += 1
    print("count",count)
    if count == lenArr:
        break
    print(i)
    temp  = sortedCars[i+k-1] - sortedCars[i]
    print("temp value",temp)
    if temp < min:
        min = temp+1
    

print("min",min)
