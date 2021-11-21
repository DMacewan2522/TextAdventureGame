tupleList = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d') ]

newTuple = []

for i in tupleList:
    if i != ():
        newTuple.append(i)

print(newTuple)