#Write a Python program to remove duplicates from a list.
a = [10,20,30,20,10,50,60,40,80,50,40]

dup_items = set()
unique_items = []

for x in a:
    if x not in dup_items:
        dup_items.add(x)
        unique_items.append(x)


print(dup_items)
print(unique_items)