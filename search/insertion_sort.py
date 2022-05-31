def insertion_sort(alias):
    for i in range(1,len(alias)):
        print("i,len",i,len(alias))
        j = i
        print("j============>",j)
        while(alias[j-1] > alias[j] and j>0):
            print(alias[j-1],alias[j])
            alias[j-1],alias[j] = alias[j],alias[j-1]
            j = j-1
    return alias
    
alias = [5,2,7,8,1,9]
print(insertion_sort(alias))