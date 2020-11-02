#Task 1

Suma = int(input("Enter Amount"))
rate = int(input("Enter rate"))
period = int(input ("Enter time"))

Profit = Suma * ( 1 + rate/100 )**period

earn = ((Profit/Suma) - 1)*100

print( round(earn,3),"%")

#Task 1 (Version 2)

Suma = int(input("Enter Amount"))
rate = int(input("Enter rate"))
period = 0
for period in  range (5):
    period += 1
    Profit = Suma * ( 1 + rate/100 )**period
    earn = ((Profit/Suma) - 1)*100
    print(round(earn,3),"%")