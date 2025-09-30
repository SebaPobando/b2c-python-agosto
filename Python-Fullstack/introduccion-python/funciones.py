# Función suma que retorna un valor y después lo imprime
def suma(a, b):
    resultado = a + b
    return resultado
    
print(suma(10, 8))

# Función resta que no retorna valor, solo imprime el resultado
def resta(a, b):
    resultado = a - b
    print("El resultado de la resta es:", resultado)
    
resta(10, 8)

def buenos_dias(nombre="alegría", cantidad=1):
   print(("Buenos días "+nombre) * cantidad)

buenos_dias()           #Imprime: "Buenos días alegría" una sola vez
buenos_dias("al amor")  #Imprime: "Buenos días al amor" una sola vez
buenos_dias(nombre="a la vida")  #Imprime: "Buenos días a la vida" una sola vez
buenos_dias(cantidad=3)  #Imprime: "Buenos días alegría" 3 veces
buenos_dias(nombre="señor Sol", cantidad=2)  #Imprime: "Buenos días señor Sol" 2 veces

#El orden de los argumentos no importa siempre y cuando especifiquemos el parámetro
buenos_dias(cantidad=3, nombre="para vos")  #Imprime: "Buenos días para vos" 3 veces
