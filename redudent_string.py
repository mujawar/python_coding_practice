# Python3 code to demonstrate working of
# Remove Reduntant Substrings from Strings List
# Using enumerate() + join() + sort()
 
# initializing list
test_list = ["Gfg", "Gfg is best", "Geeks", "Gfg is for Geeks"]
 
# printing original list
print("The original list : " + str(test_list))
 
# using loop to iterate for each string
test_list.sort(key = len)
print(test_list)
res = []
for idx, val in enumerate(test_list):
    print("idx",idx)
    print("val",val)
     
    # concatenating all next values and checking for existence
    if val not in ', '.join(test_list[idx + 1:]):
        res.append(val)
 
# printing result
print("The filtered list : " + str(res))