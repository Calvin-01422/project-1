import random


while True:
 a =  input("press y if you want to roll and n if you don't =")

     
     
 if a.lower() == "y":
   num1 = random.randint(1,6)
   num2 = random.randint(1,6)
   print(f"({num1},{num2})")
 else:
  print("no problem")
  break
