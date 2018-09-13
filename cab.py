

import random


car_wala1=["Name:Roshan singh,Ratings:4.82,Age:44"]
car_wala2=["Name:Surender singh,Ratings:4.7,Age:46"]
car_wala3=["Name:Manoj singh,Ratings:4.82,Age:46"]
print(car_wala1,car_wala2,car_wala3)
print("Select any one")
x=input()

if x==1:
    print("thanks for choosing"+car_wala1)
elif x==2:
    print("thanks for choosing"+car_wala2)
elif x==3:
    print("thanks for choosing"+car_wala3)




print("HI SIR WHAT'S YOUR NAME")
a=input()
customer_name=str(a)
print("From where you want to go sir")
from_place=input()
print("what is destination sir")
destination=input()
print("THANKS SIR FOR SUBMITTING")
print("HERE'S SOME INFORMATION ABOUT YOU:")
print("Sir Your Name is ",customer_name," \n this is current location",from_place," \n this is your destination ",destination)
otp=random.randrange(10000)
print("this is otp",otp)

print("Please Confirm your otp")
car_otp=int(input())
if otp==car_otp:
    print("continue your ride")
else:
    print("re enter the otp")
