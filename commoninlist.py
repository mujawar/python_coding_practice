def common_in_list(list1,list2):
    result = False
    for x in list1:
        print(x)
        for y in list2:
            print(y)
            if x == y:
                result = True
                return result



print(common_in_list([1,2,3,4,5], [5,6,7,8,9]))