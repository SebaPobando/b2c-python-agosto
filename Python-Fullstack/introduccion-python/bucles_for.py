# Bucle for in range simple
#for i in range(10):
    #print(i)

# Bucle for con dos argumentos
#for i in range(2, 8):
#   print(i)
   
# Bucle con tres argumentos
#for i in range(2, 12, 3):
#   print(i)
   
#for i in range(0, 15, 3):
#   print(i)

# Bucle for decrece 
#for i in range(10, 1, -3):
#   print(i)

# Bucle for para cadenas
#for l in 'Python':
#   print(l)
#for letra in 'Skillnest':
#    print(letra)
    
# Recorrer lista
#lista = ['brócoli', 'pepino', 'pimiento']

#for i in range( len(lista) ):
#   print(i, lista[i])

#Imprime: 0 brócoli, 1 pepino, 2 pimiento

#for verdura in lista:
#   print(verdura)
#Imprime: brócoli, pepino, pimiento

#Recorrer tuplas usando bucle for
#tupla = ('fresa', 'manzana', 'cereza')

#for i in range( len(tupla) ):
#   print(i, tupla[i])

#Imprime: 0 fresa, 1 manzana, 2 cereza

#for fruta in tupla:
#   print(fruta)
#Imprime: fresa, manzana, cereza

# Imprimir SOLO cada una de las claves del diccionario
estudiante = {
    "nombre": "Gonzalo", 
    "curso": "Python"
    }
for clave in estudiante:
   print(clave)
#Imprime: nombre, curso

# Imprimirá SOLO los valores de las claves del diccionario
for valor in estudiante:
   print(estudiante[valor])
#Imprime: Gonzalo, Python

for clave_valor in estudiante:
    print(clave_valor + ":", estudiante[clave_valor])
