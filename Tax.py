print("Tax Calculator")
ain=(float(input("Enter your annual income: ")))
if ain <=250000:
    taxrate=0
    taxamount=0
    print("No tax applicable")
elif ain<=500000:
    taxrate=5
    taxamount=ain*(taxrate/100)
elif ain<=1000000:
    taxrate=20
    taxamount=ain*(taxrate/100) 
elif ain>1000000:
    taxrate=30
    taxamount=ain*(taxrate/100)
print("Annual Income: ",ain)
print("Tax Rate: ",taxrate,"%")
print("Tax Amount: ",taxamount)
