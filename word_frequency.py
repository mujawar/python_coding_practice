#Get word frequency - initializing dictionary
from ast import operator


ss = """Nory was a Catholic because her mother was a Catholic, 
and Nory's mother was a Catholic because her father was a Catholic, 
and her father was a Catholic because his mother was a Catholic, 
or had been."""

word = ss.split()
print(word)

d = {x:0 for x in word}
print(d)
for w in word:
    d[w] +=1

print(d)

#second method
# d = {}
# for w in word:
#     d[w] = d.get(w,0) +1

# print(d)
