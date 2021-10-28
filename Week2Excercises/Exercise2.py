words = ["xxx", "aaa", "r5t6yy", "g", "wow"]

counter = 0

for items in words:
    if len(items) >= 2 and items[0] == items[-1]:
        counter += 1

print(counter)