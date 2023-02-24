#script for car prices
#import numpy as np
cars = dict()
cars["bugatti"] =200000
cars["audi"] =80000
cars[" GMC"] =20000
cars["tesla"] =80000
cars["Honda"] =2000
cars["lucid"] =5000
cars["ascent"] =9000
cars["atlas"] =4000
cars["artura"] =3500
cars["avalon"] =4000
cars["bentley"] =9000
cars["punani astra"] =3000
cars["dodge"] =502000
cars["jeep"] =803000
cars["lincoln"] =2500
cars["porsche"] =405000
cars["mazda"] =30000
cars["cadillac"] =7000
cars["genesis"] =7000
cars["sonata"] =55000
cars["buick"] =45000
cars["hyundai"] =4000
cars["mazda"] =7000
cars["tesla"] =9000
cars["maserati"] =80000
cars["opel zafira"] =1000
cars["audi"] =3000
cars["lamborghini"] =60000
cars["range rover"] =70000
cars["tata"] =2000
cars["land rover"] =9000
cars["renault"] =7000

print("Welcome to OH WOW's car dealership")

print("Which car would you like to purchase?")

order = input()
if cars.get(order):
    print("The "+order+" costs $" + str(cars.get(order)))
else:
    print("Sorry "+order+" is unavialable")
    
 https://github.com/papakofii/car-6926321.git
