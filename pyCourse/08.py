phrase = input("Type a phrase: ")
letter = input("Type a character what u want to finish the loop")
dictionary = ("a","b","c","d")

for i in phrase:
    if i == letter:
        break
    elif i in dictionary:
        continue
    print(i, end=" ")

# string = input("Introduce una frase estimado: ")
# string_end = input("Ahora, ¿Con que letra deseas terminar el bucle? ")
# print()
# for letter in string:
#     if letter.lower() == string_end.lower():
#         break
#     elif letter.lower() in ("a","e","i","o","u"):
#         continue
#     print(letter,end="")