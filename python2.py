# for loop in python

for i in range(5):
    print(i)

print("Loop ended")


fruits = ["apple","banana","grapes","watermelon","guava","pomegrenade"]

for items in fruits:
    print(items)



# while loop in python

j = 0

while(j<10):
    print(j+1)
    j += 1

print("Loop ended")



# Functions in python

def Average(num1,num2,num3):

    avg = (num1+num2+num3)/3

    print("Average is ",avg)

    return avg


print("Executing")

store = Average(45,85,12)

print("Store = ",store)

print("Execution Done...")



