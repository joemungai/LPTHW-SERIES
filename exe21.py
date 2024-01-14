def add(a,b):
    print (f"ADDING {a} + {b}")
    return a + b
def subtract (a,b):
    print (f"SUBTACSTING {a} - {b}")
    return a - b
def multiply(a,b):
    print(f"multiplying {a} * {b}")
    return a * b
def divide (a,b):
    print(f"DIVIDING {a} / {b}")
    return a / b
print ("lets do some math with just functions!")
age = add (30,5)
height = subtract(78,4)
weight = multiply(90,2)
iq = divide(100,2)
print("here is a puzzle .")
what = add(age,subtract(height,multiply(weight,divide(iq,2))))
print("that becomes ", what ,"Can you do it by hand?")
