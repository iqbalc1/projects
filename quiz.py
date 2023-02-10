print("Welcome to the mathematic quiz")
choice=input("Do you want to start the quiz?  ")
result=0
if choice != "yes":
     quit()
print("Ok, Great! Lets Play")

answer= input("Q No.1  Find the value of 'x', if 2x=6 " )
if answer==("3"):
    print("Correct")
    result+=1
else:
    print("Incorrect")

answer= input("Q No.2  Find the value of y, if 2y + 3y = 5 " )
if answer==("1"):
    print("Correct")
    result+=1
else:
    print("Incorrect")

answer= input("QNo.3  Find the value of 'x', if logx = 2 " )
if answer==("100"):
    print("Correct")
    result+=1
else:
    print("Incorrect")

answer= input("QNo.4  Is 2*2 matrix, a square matrix? Yes/No  " )
if answer.lower()==("yes"):
    print("Correct")
    result+=1
else:
    print("Incorrect")

answer= input("Q No.5  Factorize, 2x+4  " )
if answer==("2(x+1)"):
    print("Correct")
    result+=1
else:
    print("Incorrect")

print("You got "+ str(result) + "/5 marks")
print("You got "+ str((result/5)*100) + "% ")







# score=0

# 
#     score+=1
# else:
#     print ("Incorrect!")

# answer= input("What is the value of y, if 3y+2y=5 " )
# if answer==("1"):
#     print ("Correct!")
#     score+=1
# else:
#     print ("Incorrect!")

# answer= input("What is the value of 'pi' in maths " )
# if answer==("3.14"):
#     print ("Correct!")
#     score+=1
# else:
#     print ("Incorrect!")

# answer= input("Is it True 2+5<8 write yes or no " )
# if answer.lower()==("yes"):
#     print ("Correct!")
#     score+=1
# else:
#     print ("Incorrect!")

# answer= input("F = " )
# if answer.lower()==("ma"):
#     print ("Correct!")
#     score+=1
# else:
#     print ("Incorrect!")

# print("You have got "+ str(score) + " correct answers")
# print("You got "+ str((score/5)*100) + "% ")
