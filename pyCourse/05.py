frase = input("Introduce una frase: ")
eliminar = input("Introduce la palabra que deseas eliminar: ")
substring = ""

indice = frase.find(eliminar)
substring = frase[0:indice] + frase[indice+len(eliminar)+1: ]
print(substring)