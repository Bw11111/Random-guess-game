import random
num = input("Enter a number...   ")
num2 = input("Enter range(max is 1000)...   ")
if int(num2) > 1000:
  print("")
else:
  def rand():
    ran1 = random.randint(1,int(num2))
    if ran1 == int(num):
      print(num)
      print("Number Guessed! Number is " + str(ran1))
    else:
      print(ran1)
      rand()
  rand()