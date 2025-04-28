
class Calculator:
    
    def __init__(self):
        pass

    def add(self, a, b):
        return a + b

    def subtract(self, a, b): 
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Error: División por cero"

    def modulo(self, a, b):
        return a % b


if __name__ == "__main__":
    my_calculator = Calculator()
    su_calculator = Calculator()
    print(my_calculator.add(5, 7))
    print(my_calculator.subtract(45, 11))
    print(my_calculator.multiply(3, 2))
    print(su_calculator.divide(10,0))