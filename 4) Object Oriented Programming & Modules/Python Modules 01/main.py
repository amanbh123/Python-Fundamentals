import calculator
# from calculator import add
# from calculator import *
# from calculator import (add, sub)

print(type(calculator))
print(type(calculator.add))

print(calculator.CONSTANT)

print(calculator.add(4, 7))
print(calculator.sub(4, 7))
print(calculator.mul(4, 7))
print(calculator.div(4, 7))

a = calculator.A()
print(type(a))