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

#Task 2
price =  500/1000
Chesee = 0
for Chesee in range (50,1050):
      if Chesee >= 25 and Chesee%50==0: 
            cost = Chesee * price
            print('Chesee: {gram}  Price: {kilo}'.format(gram = Chesee, kilo = cost ))
#Task3
n = int(input("Start of the interval"))
m = int(input("End of the interval"))
print(f"all interval {n} - {m}")
i = 0
for i in range (n,m):
    i += 1
    if i%2==0:
        print("divide-",i)
    else:
        print("indivisible-",i)

#Task4
import string
i=list(string.ascii_lowercase)
print(i)
print(len(i))
#Task5
# There is number no letter.
number_letter = int(input("what is you the best number from 0- 26?"))
import string
string.ascii_lowercase[number_letter]
print("previously letter", string.ascii_lowercase[number_letter-1])
print("next letter",string.ascii_lowercase[number_letter+1])


#Task6
friend_name=input()
Friends =["Andy","Thomas","Jack","Adam","Paras"]
if friend_name in Friends:
    print("Hello, Gosza")
else:
    print("Hello, Gosza Goszowicz")

#Task5 part1
n =int(input("enter the string-->"))
a = n // 10
b = n%10
c=n//100
d=c//1000
print( a+b+c+d)
print(n)

#Task5 part2
n =input("enter the string-->")
countn = 0
for i in n:
    if i.isdigit():
        countn +=1
    else:
        countn +=1
        print("The number of numbers are NONE")
print("The number of numbers are",countn)