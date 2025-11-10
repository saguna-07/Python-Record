try:
    x=int("str")
    inv=1/x
except ValueError:
    print("Not Valid! Give only integer input")
except ZeroDivisionError:
    print("Zero has no inverse!")


