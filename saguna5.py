import random
value=random.choice(["h","t"])
choice=input("Make your choice!!(h or t)").lower()
if value==choice:
    print("You win")
else:
    print("bad luck")
if value=="h":
    print("The computer selected heads")
elif value=="t":
    print("The computer selected tails")
