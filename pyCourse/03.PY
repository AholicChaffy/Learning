n1 = int(input("Introduce un numero: "))
n2 = int(input("Introduce un numero: "))
n3 = int(input("Introduce un numero: "))


if n1 > n2 and n1 > n3:
    print(f"{n1} es el numero mayor")
else: 
    if n2 > n1 and n2 > n3:
        print(f"{n2} es el mayor")
    else:
        print(f"{n3} es el mayor")