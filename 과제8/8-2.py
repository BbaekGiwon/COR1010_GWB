D = {'c': 7, 'f': 3, 'a': 5}
a= []
for i in sorted(D):
    a.append((i, D[i]))
print("After sort :", a)
