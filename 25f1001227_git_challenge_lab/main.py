# main.py - simple CLI for arithmetic
from sum_module import add
from diff_module import subtract
from product_module import multiply

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def main():
    print("=== Arithmetic Project (25f1001227) ===")
    a = get_number("Enter first number: ")
    b = get_number("Enter second number: ")
    print()
    print("Sum:       ", add(a, b))
    print("Difference:", subtract(a, b))
    print("Product:   ", multiply(a, b))
    print("\\nThank you.")
if _name_ == '_main_':
    main()
