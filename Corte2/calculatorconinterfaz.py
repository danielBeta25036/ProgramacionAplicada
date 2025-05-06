import tkinter as tk
from tkinter import messagebox

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

class CalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")
        
        self.calculator = Calculator()
        
        # Entrada de datos
        self.entry1 = tk.Entry(self.root, width=15, font=("Arial", 14))
        self.entry1.grid(row=0, column=0, padx=5, pady=5)
        
        self.entry2 = tk.Entry(self.root, width=15, font=("Arial", 14))
        self.entry2.grid(row=0, column=1, padx=5, pady=5)
        
        # Etiqueta de operaciones
        self.operation_label = tk.Label(self.root, text="Selecciona operación:", font=("Arial", 12))
        self.operation_label.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
        
        # Botones para seleccionar la operación
        self.add_button = tk.Button(self.root, text="+", width=5, height=2, font=("Arial", 14), command=self.add)
        self.add_button.grid(row=2, column=0, padx=5, pady=5)
        
        self.subtract_button = tk.Button(self.root, text="-", width=5, height=2, font=("Arial", 14), command=self.subtract)
        self.subtract_button.grid(row=2, column=1, padx=5, pady=5)
        
        self.multiply_button = tk.Button(self.root, text="*", width=5, height=2, font=("Arial", 14), command=self.multiply)
        self.multiply_button.grid(row=3, column=0, padx=5, pady=5)
        
        self.divide_button = tk.Button(self.root, text="/", width=5, height=2, font=("Arial", 14), command=self.divide)
        self.divide_button.grid(row=3, column=1, padx=5, pady=5)
        
        self.modulo_button = tk.Button(self.root, text="%", width=5, height=2, font=("Arial", 14), command=self.modulo)
        self.modulo_button.grid(row=4, column=0, padx=5, pady=5)

        # Botón de resultado
        self.result_button = tk.Button(self.root, text="Calcular", width=10, height=2, font=("Arial", 14), command=self.calculate)
        self.result_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

        # Etiqueta de resultado
        self.result_label = tk.Label(self.root, text="Resultado: ", font=("Arial", 14))
        self.result_label.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

    def get_values(self):
        try:
            a = float(self.entry1.get())
            b = float(self.entry2.get())
            return a, b
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese valores numéricos válidos.")
            return None, None

    def add(self):
        a, b = self.get_values()
        if a is not None and b is not None:
            result = self.calculator.add(a, b)
            self.show_result(result)

    def subtract(self):
        a, b = self.get_values()
        if a is not None and b is not None:
            result = self.calculator.subtract(a, b)
            self.show_result(result)

    def multiply(self):
        a, b = self.get_values()
        if a is not None and b is not None:
            result = self.calculator.multiply(a, b)
            self.show_result(result)

    def divide(self):
        a, b = self.get_values()
        if a is not None and b is not None:
            result = self.calculator.divide(a, b)
            self.show_result(result)

    def modulo(self):
        a, b = self.get_values()
        if a is not None and b is not None:
            result = self.calculator.modulo(a, b)
            self.show_result(result)

    def calculate(self):
        a, b = self.get_values()
        if a is not None and b is not None:
            result = f"{a} y {b} no son suficientes para calcular una operación"
            self.show_result(result)
        
    def show_result(self, result):
        self.result_label.config(text=f"Resultado: {result}")

if __name__ == "__main__":
    root = tk.Tk()
    gui = CalculatorGUI(root)
    root.mainloop()
