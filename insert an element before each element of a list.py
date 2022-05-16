color = ['Red', 'Green', 'Black']

print("original list",color)

final = [v for elt in color for v in ('c',elt)]


print("final",final)
