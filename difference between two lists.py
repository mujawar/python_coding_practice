from collections import Counter
color1 = ["red", "orange", "green", "blue", "white"]
color2 = ["black", "yellow", "green", "blue"]

c1=Counter(color1)
c2=Counter(color2)

print(list(c1-c2))