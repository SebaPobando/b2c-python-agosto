# num = 0

# while num < 4:
#    print("bucle while -", num)
#    num += 1
# else:
#     print("¡Acabas de salir del bucle!")

# for letra in "detente":
#    if letra == "n":
#        break
#    print(letra)

# for letra in "detente":
#    if letra == "n":
#         continue
#    print(letra)

x = 6

while x > 2:
   print(x)
   x -= 1
   if x == 3:
       break
else: #Recuerda: Solo se ejecuta en una salida normal, NO en un break
   print("Sentencia final")