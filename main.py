import random

from colorama import Fore
account = 1000
#font = pyfiglet.figlet_format("\n wellcome to rafi casino ! be multi billioner \n")
#print(font)
print(Fore.YELLOW+"\n wellcome to rafi casino ! be multi billioner \n")
print(Fore.YELLOW+"\n rules are simple , if you won you will get double if you lose you will lose bet ammount\n")
print(Fore.MAGENTA+"\nyour account has 1000$ , so be carefull\n")
while True:
  ask = int (input(Fore.CYAN +"how much do you want to bet :"))
  if ask > account:
    print(Fore.RED+"\nyou dont have enough money\n")
    continue
  a = random.randint(1,2)
  b = random.randint(1,2)
  c = random.randint(1,2)
  print("\n", a,b,c, "\n")
  if a == b == c:
    print(Fore.GREEN + "\n congratulations ! you won", ask*2 ,"dollars\n")
    account += ask*2
    print(Fore.GREEN +"your current balance is ", account ,"dollars")
  else:
    print(Fore.RED + "\n ohh nooo ! you lost ", ask , " dollars\n")
    account -= ask
    print(Fore.RED +"your current balance is ", account ,"dollars")
  j = input(Fore.BLUE + " do you want to play again (y/n) :")
  if j == "y":
    continue
  else:
   print(Fore.GREEN + "\n thank you for playing ! your final balance is ", account ,)
   break
