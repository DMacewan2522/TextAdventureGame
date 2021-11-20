months = {	'01':'Janauary','02':'February','03':'March','04':'April','05':'May','06':'June',
   '07':'July','08':'August','09':'September','10':'October','11':'November','12':'December'}

days = ["1", "2", "3", "4", "5", "6", "7", "8", "9",
        "10", "11", "12", "13", "14", "15", "16", "17",
        "18", "19", "20", "21", "22", "23", "24", "25",
        "26", "27", "28", "29", "30", "31"]

programOn = True

while programOn != False:
    dateInput = input("Please enter the date: ")
    dateSplit = dateInput.split("/")
    for dayNumber in days:
        if dateSplit[0] == dayNumber:
            print("The date is,", dateSplit[0], months.get(dateSplit[1]), dateSplit[2])
            programOn = False
            break
    else:
        print("Enter a valid date. Eg. 11/09/1992")
        continue