fname = input('First name: ')
lname = input('Last name: ')
print(lname+" "+fname)

print ('\n###Diferent method###\n')
#create a list with the string and split when occour a space
name = fname+" "+lname
x = name.rsplit(" ")

for o in reversed(x):
    print(o)