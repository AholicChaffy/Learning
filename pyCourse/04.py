print("Calculadora")

print("""Menu de opciones
      1 Suma
      2 Resta
      3 Multiplicacion
      4 Division
      5 Division Entera
      6 Exponente
      7 Modulo o resto""")

option = int(input("Selecciona una opcion: "))

if option == 1:
    x = int(input("Introduce el primer numero: "))
    x += int(input("Introduce el segundo numero: "))
    print(f"El resultado es: {x}")
elif option ==2:
    x = int(input("Introduce el primer numero: "))
    x -= int(input("Introduce el segundo numero: "))
    print(f"El resultado es: {x}")
elif option ==3:
    x = int(input("Introduce el primer numero: "))
    x *= int(input("Introduce el segundo numero: "))
    print(f"El resultado es: {x}")
elif option ==4:
    x = float(input("Introduce el primer numero: "))
    x /= float(input("Introduce el segundo numero: "))
    print(f"El resultado es: {x}")
elif option ==5:
    x = int(input("Introduce el primer numero: "))
    x //= int(input("Introduce el segundo numero: "))
    print(f"El resultado es: {x}")
elif option ==6:
    x = int(input("Introduce el primer numero: "))
    x **= int(input("Introduce el segundo numero: "))
    print(f"El resultado es: {x}")
elif option ==7:
    x = int(input("Introduce el primer numero: "))
    x %= int(input("Introduce el segundo numero: "))
    print(f"El resultado es: {x}")
else:
    print("Opcion invalida")