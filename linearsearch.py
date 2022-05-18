def linear_search(list,key):
    # print(type(list),type(key))
    for i in range(len(list)):
        print(i)
        if list[i] == key:
            return i
    return -1




inext = linear_search([1,2,3,4,5,6],10)
print(f"the element {10} preset at the index {inext}")