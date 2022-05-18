x = ["mango","orange","mango","apple"]
y = ["mango","orange","mango","dog"]
z = ["mango"]
setx = set(x)
sety = set(y)
setz = set(z)
print(x)
print(setx)


print(setz.issubset(setx))
print(setx.issuperset(setz))