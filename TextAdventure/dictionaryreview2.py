room_items = {"item1" : {"Name" : "Lamp", "Colour" : "Red"},
              "item2" : {"Name" : "Table", "Colour" : "Brown", "Type" : 0},
              "item3" : {"Name" : "Lamp", "Colour" : "Red"},
              "item4" : {"Name" : "Chair", "Colour" : "Green", "Type" : 1},
              }

noDuplicates = {}

for key,value in room_items.items():
    if value in noDuplicates.values():
        continue
    else:
        noDuplicates[key] = value

print(noDuplicates)