def basic(age, months):
    print("Basic Membership")
    print("Fee: 1000 ruppes per month")
    tf = 1000 * months
    if months >= 6:
        discount = tf * 0.1
        tf -= discount
    elif months >= 12:
        discount = tf * 0.2
        tf -= discount   
    return tf 
        

def premium(age, months):
    print("Premium Membership")
    print("Fee: 2000 ruppes per month")
    tf = 2000 * months
    if months >= 6:
        discount = tf * 0.1
        tf -= discount
    elif months >= 12:
        discount = tf * 0.2
        tf -= discount
    return tf
       

def vip(age, months):
    print("VIP Membership")
    print("Fee: 5000 ruppes per month")
    tf = 5000 * months
    if months >= 6:
        discount = tf * 0.1
        tf -= discount
    elif months >= 12:
        discount = tf * 0.2
        tf -= discount    
    return tf

        
def vip(age, months):
    print("VIP Membership")
    print("Fee: 5000 ruppes per month")
    tf = 5000 * months
    if months >= 6:
        discount = tf * 0.1
        tf -= discount
    elif months >= 12:
        discount = tf * 0.2
        tf -= discount
    return tf
        

name=input("Enter your name: ")
age=int(input("Enter your age: "))
months=int(input("Enter the number of months you want to subscribe: "))
print("Welcome to the Gym Membership Calculator")
print("Select the type of membership you want to calculate:")
print("1. Basic Membership")
print("2. Premium Membership")
print("3. VIP Membership")
choice=int(input("Enter your choice: "))
if choice==1:
    x= basic(age, months)
    print("Total fee for Basic Membership: ", x, "rupees")
elif choice==2:
    x= premium(age, months)
    print("Total fee for Premium Membership: ", x, "rupees")
elif choice==3:
    x= vip(age, months)
    print("Total fee for VIP Membership: ", x, "rupees")
else:
    print("Invalid choice")

    

