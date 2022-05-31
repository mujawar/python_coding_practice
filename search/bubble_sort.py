def bubble_sort(list1):
    for i in range(len(list1)-1,0,-1):
        print("i",i)
        no_swap = True
        for j in range(0,i):
            print("j",j)
            if list1[j+1] < list1[j]:
                print("j+1,j",list1[j+1] ,list1[j])
                list1[j],list1[j+1] = list1[j+1],list1[j]
                print("list1",list1)
                no_swap = False

        if no_swap:
            return list1


list1 = [3,4,7,1,8,2]
print(bubble_sort(list1))