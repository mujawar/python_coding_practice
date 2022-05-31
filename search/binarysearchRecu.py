def binary_search_recursion(list1,start,end,key):
    while start < end:
        mid = (start + end) // 2
        print("mid",mid)
        if list1[mid] > key:
            return binary_search_recursion(list1,start,mid,key)
        elif list1[mid] < key:
            return binary_search_recursion(list1,mid+1,end,key)
        else:
            return mid
    return -1



lista = [1,2,3,4,5,6,7]
key = 5
index = binary_search_recursion(lista,0,len(lista),key)
print(f"the element {key} preset at the index {index}")