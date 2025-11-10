import random
colour=random.choice(["black","white","blue","red","yellow"])
correct=False
while correct==False:
    guess=input("Pick on colour:black,white,blue,red,yellow").lower()
    if guess==colour:
        print("Well done")
        correct=True
    else:
        if colour=="black":
            print("You are such a black luck guy")
        if colour=="white":
            print("Too naive to choose white")
        if colour=="blue":
            print("You probably feeling blue right now")
        if colour=="red":
            print("is your face looks red right now")
        if colour=="yellow":
            print("I bet your future is as bright as yellow")
