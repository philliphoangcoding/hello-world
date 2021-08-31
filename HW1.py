print("Birthday Calculator")
print("Current day")
cmonth = int(input("Month: "))
cday = int(input("Day: "))
cyear = int(input("Year: "))
print("Birthday")
bmonth = int(input("Month: "))
bday = int(input("Day: "))
byear = int(input("Year: "))
value1 = cyear-byear-1
if cmonth == bmonth and cday > cday:
    value1 += 1
elif cmonth > bmonth:
    value1 += 1
if cmonth == bmonth and cday == bday:
    value1 += 1
print("You are",value1,"years old.")
if cmonth == bmonth and cday == bday:
    print("Happy Birthday!")