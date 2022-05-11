# my_list = [2, 3, 5, 7, 11]
# # squarelist = [x**2 for x in my_list]
# congsquare = [x for x in my_list if x%2!=0]
# # print(squarelist)
# print(congsquare)

# # dictlist = {y:y**2 for y in my_list}
# dictlist = {y**2 for y in my_list if y%2!=0}
# print(dictlist)


#Combining multiple lists into one
# a = [1, 2, 3]
# b = [7, 8, 9]

# result = [(x+y) for (x,y) in zip(a,b)]
# print(result)

# nested iterators
a = [1, 2, 3]
b = [7, 8, 9]
result = [(x,y) for x in a for y in b]
print(result)