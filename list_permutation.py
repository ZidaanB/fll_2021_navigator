import itertools
pp = list(itertools.permutations(["a","b","c","d"]))
print(type(pp))
print(len(pp))
print(pp)
for i in range(0,len(pp)):
    print(pp[i])

