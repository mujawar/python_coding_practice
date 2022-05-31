def binary_search(lista,key):
    start =0
    end = len(lista)
    while start <= end:
        mid = (start + end) // 2
        print(mid)
        if lista[mid] == key:
            return mid
        elif lista[mid] < key:
            start = mid
        else:
            end=mid
    return -1

key = 2
index = binary_search([1,2,3,4,5,6],key)
print(f"the element {key} preset at the index {index}")