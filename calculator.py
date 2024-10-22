def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "No se puede dividir entre cero"
    return x / y

def calculator():
    print("Selecciona la operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

    choice = input("Elige una opción (1/2/3/4): ")
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))

    if choice == '1':
        print(f"Resultado: {add(num1, num2)}")
    elif choice == '2':
        print(f"Resultado: {subtract(num1, num2)}")
    elif choice == '3':
        print(f"Resultado: {multiply(num1, num2)}")
    elif choice == '4':
        print(f"Resultado: {divide(num1, num2)}")
    else:
        print("Opción no válida")

if __name__ == "__main__":
    calculator()
