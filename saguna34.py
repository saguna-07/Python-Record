try:
    n=0
    res=100/0
except ZeroDivisionError:
    print("you can't divide by Zero!")
    n = int(input('enter value '))
    res = 100 / n
    print(res)
except ValueError:
   print("Enter a valid number!")
else:
   print("Result is", res)
finally:
   print("Execution complete.")
