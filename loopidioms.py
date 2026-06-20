#largest number in a list
z=-1
for n in [5,21,45,23,67,4,4,665,3,2,56,]:
    if n>z:
        z=n
print(z)
#counting the number of elements in a list
z=0
for x in [5,21,45,23,67,4,4,665,3,2,56]:
    z=z+1
print(z)
#smallest number in a list
z=None
for x in [5,21,45,23,67,4,4,665,3,2,56]:
    if z is None :
        z=x
    elif x<z:
        z=x
print(z)
