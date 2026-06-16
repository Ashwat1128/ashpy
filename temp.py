print("Temperature converter")
temp=float(input("Enter temperature in celsius: "))
f=(9/5)*temp+32
print("Temperature in fahrenheit is: ",f)
if f>100:
    print("HOT")
elif f<0:
    print("COLD")
else :
    print("NORMAL")
    