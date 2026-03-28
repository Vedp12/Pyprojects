import string
import random

def pass1(length):
    char=string.ascii_lowercase+string.ascii_uppercase
    Symbol = input("DO you want symbol?  ")
    if Symbol == "y" or Symbol == "yes":
        char += string.punctuation
    else:
        pass  
    for i in range(length): 
        ran = random.choice(char)
        print(ran , end="")
user_inp=int(input("Enter number: "))
pass1(user_inp)
