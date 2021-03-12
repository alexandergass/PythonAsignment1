#!/usr/local/bin/python3
import math;

while True:
    myInput = input("Enter a real (decimal) number: ");

    try:
        float(myInput);
        convertedNumber = float(myInput);
        if convertedNumber%1!=0:
            print(convertedNumber," is a real (decimal) number");
            print("Ceil: ", math.ceil(convertedNumber));
            print("Floor: ", math.floor(convertedNumber));
            print("Round: ", round(convertedNumber));
            break;
        else:
            print(convertedNumber," is not a real (decimal) number");
    except:
        print(myInput," is not a number");

