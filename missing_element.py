test_list = [3, 5, 6, 8, 10]
  
# printing original list
print("The original list : " ,test_list)

# res = [ele for ele in range(max(test_list)+1) if ele not in test_list]
# print(res)

#second method
test1 = set(range(max(test_list)+1))
test2 = set(test_list)
print(test1)
print(test2)
res = list(set(range(max(test_list)+1)) - set(test_list))
print(res)