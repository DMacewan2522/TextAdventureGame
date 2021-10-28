x = ['mix', 'xyz', 'apple', 'xanadu', 'rovio']

itemsWithX = []
itemsNoX = []

finalList = []

for letter in x:
    if 'x' in letter[0]:
        itemsWithX.append(letter)
    else:
        itemsNoX.append(letter)

itemsWithX.sort()
itemsNoX.sort()

finalList = itemsWithX + itemsNoX

print(finalList)