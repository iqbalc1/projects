import random
print("Welcome to the guessing game !")
print("Meray Zehan main aik number hay 1-20 k darmyan guess karain!")
print("Ap guess kar sakty hain? ")

number= random.randint(1,20)
guess=0
totalguess=0
# aik hi kam ap nay bar bar repeat karna ho to loop lagana hay
# for, while
# agar hamara guess, number k equal nahi hay
while guess!=number:
    guess= int(input("Number Guess karain . . . "))
    totalguess+=1
#shart
    if guess<number:
        print("Oh, Ap ka number bht chota hay")
    elif guess>number:
        print("Ah, Ap ka number bht bara hay")
    else:
        print(f"Wow,,, Great! Ap ka guess theek hay. lekin ap nay total {totalguess} guess lagaiy!")







