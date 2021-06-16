num=int(input("guess number"))
import random
num2=random.randint(1,10)
while num!=num2:
    print("no")
    num=int(input("guess number"))
print("yes")

