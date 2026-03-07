num = int(input("enter the number"))
unit = input("enter the unit")
def Unitconverter(num,unit):
    if unit == "mm":
        num = num/1000
    elif unit == "cm":
        num = num/100
    else:
        print("in meters")

    return num,unit
run = Unitconverter(num,unit)
print(run)