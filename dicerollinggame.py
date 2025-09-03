import random
num1 = random.randint(1,6)
num2 = random.randint(1,6)
a =  input("press y if you want to play and n if you don't")

if a == "y" or a == "Y":
 print(f"({num1},{num2})")
else:
 print("no problem")