"""""
Jalen Banks
lab 9, Unit Testing
Feb 26. 2026
"""""

def addthreenumbers(n1=0,n2=0,n3=0):
    return n1 + n2 + n3
def subtracttwonumbers(n1=0,n2=0):
    return n1 - n2
def multiplytwonumbers(n1,n2,n3):
    return n1 * n2 * n3
def dividetwonumbers(n1,n2):
    try:   
        return n1 / n2
    except ZeroDivisionError:
        print("ERROR!: Cannot divide by zero.")
    except ValueError:
        print("ERROR!: Invalid input. Please enter numbers only.")
    except:
        print("ERROR!: cannot divide the numbers.")