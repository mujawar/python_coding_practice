def selection_sort(list1):
    for i in range(0,len(list1) -1):
        print("i",i)
        smallest = i
        for j in range(i+1,len(list1)):
            print("j",j)
            if list1[j] < list1[smallest]:
                smallest = j
            list1[i],list1[smallest] = list1[smallest],list1[i]
    return list1



list1 = [3,4,7,1,8,2]
print(selection_sort(list1))