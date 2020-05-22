# Homework 4 - Ben Grudzien
# ENG 1503 - Voltage Divider Calculator

#import sys (Gets rid of "none" for other script)

def voltage_divider(Vin, R1, R2):
    try:
        return (Vin * R2) / (R1 + R2)
    except ZeroDivisionError:
        print("Error: Can't divide by 0")
    
print("--- VOLTAGE DIVIDER CALCULATOR ---\n")
input('Press ENTER to begin')

while True:
    
    print("What is the input voltage, Vin?")
    Vin = int(input())
    print("What is R1's value?")
    R1 = int(input())
    print("What is R2's value?")
    R2 = int(input())
    print("The output voltage = ", voltage_divider(Vin, R1, R2))
    input("\nPress ENTER to restart (CTRL+C to exit)\n")



