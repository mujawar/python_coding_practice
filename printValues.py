def printValues1():
    l = list()
    for i in range(1,21):
        # print(i)
        l.append(i**2)
    print(l[:5])
    print(l[-5:])


print(printValues1())