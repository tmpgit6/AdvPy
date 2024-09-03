
try:
    num1 = int(input("Num1: ")) 
    num2 = int(input("Num1: ")) 
    total = num1 / num2 

except ValueError:
    print("[ErrorNr: 1001] Inputs should be between 0-9")

except ZeroDivisionError:
    print("[ErrorNr: 1002] Num2 should not be zero")

except Exception as e:
    print("[ErrorNr: 8000] Something wrong happend:\n", e) 

except BaseException as e:
    print("[ErrorNr: 9000] Something wrong happend:\n", e) 
 
else:
    print("Total:", total)

finally:
    print("Vielen Dank")