# Printing first hello world program in python 

print("Hello World")

# print('Hiiii World')

# IN python single line comment is achieved by '#'
# For multiline comment we use '''message'''


# Variables in python

a = 5
b = 6.6
c = False # or True
d = "Sunit"
e = None


# Typecasting in python

var = "5"
print(int(var)+5) # op -> 10



# Operators in python (some special)

print(2 ** 4) # power operator

print(5 // 3) # point k baad jo rahega wo nhi dikhayega


# Logical Operators

# && -> and

# || -> or

# ! -> not




# Conditionals in python

if(5>10):
    print("NO")
elif(5 == 10):
    print("NEVER")
else:
    print("YES")
    print("yes2")




# User Input in python

#input function always accepts value as a string

name = input("Enter your name : ")
print(type(name),name)

num = int(input("Enter a number : "))
print(type(num), num + 100)



# Switch Case in python

n = 5

match n:
    case 1:
        print("In Case 1")
    case 2:
        print("In Case 2")
    case 3:
        print("In Case 3")
    case 4:
        print("In Case 4")
    case 5:
        print("In Case 5")
    case _:
        print("In Default")



