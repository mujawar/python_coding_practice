from importlib_metadata import functools


l = [x for x in range(10) if x %2 ==0]
print(l)


mlist = list(filter(lambda x:x%2 ==0, [x for x in range(20)]))
print("mlist",mlist)

o = list(map(lambda x : x**2,mlist))
print(o)
import functools
temp = functools.reduce(lambda x,y:x+y,mlist)
print(temp)