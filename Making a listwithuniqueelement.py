dup_list = [1,2,3,4,4,4,5,1,2,7,8,8,10]

templist = list(set(dup_list))
print(templist)

#second method

d = {k:0 for k in dup_list}
print(d)

for x in dup_list:
    d[x] += 1

print(d)

unq =[ k for k,v in d.items() if v==1]
print(unq)