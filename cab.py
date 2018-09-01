

import random


car_wala1=["Name:Roshan singh,Ratings:4.82,Age:44"]
car_wala2=["Name:Surender singh,Ratings:4.7,Age:46"]
car_wala3=["Name:Manoj singh,Ratings:4.82,Age:46"]
print(car_wala1,car_wala2,car_wala3)
print("Select any one")
x=input()
x-=1
if x==0:
    print("thanks for choosing"+car_wala1)
if x==1:
    print("thanks for choosing"+car_wala2)
if x==2:
    print("thanks for choosing"+car_wala3)



print(car_wala)
print("HI SIR WHAT'S YOUR NAME")
a=input()
customer_name=str(a)
print("From where you want to go sir")
from_place=input()
print("what is destination sir")
destination=input()
print("THANKS SIR FOR SUBMITTING")
print("HERE'S SOME INFORMATION ABOUT YOU:")
print(customer_name," \n ",from_place," \n ",destination)
