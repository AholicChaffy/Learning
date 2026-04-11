table = int(input("Que tabla de multiplicar quieres?: "))

for i in range(0,11):
    result = i * table
    print(f"{table}x{i}={result}")