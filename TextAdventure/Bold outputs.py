a_list = [3, 5, 6, 12]

print("\033[1m", a_list[0])
print("\033[1m", a_list[1:])

reverseda_list = []

for i in reversed(a_list):
    reverseda_list.append(i)

print("\033[1m", reverseda_list)

multiplieda_list = []

for i in a_list:
    multiplieda_list.append(i*3)

print(multiplieda_list)

booleanList = []

for i in a_list:
    if i%2 != 0:
        booleanList.append("False")
    else:
        booleanList.append("True")

print(booleanList)