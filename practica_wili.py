


#Ejercicio 12

#Ejercicio 11


print("\n\n")


#Ejercicio 10
payaso_peso = 112 #g
muñeca_peso =75 #g

payasos = int(input("Cuantos payasos tiene el pedido: "))
muñecas = int(input("Cuantas muñecas tiene el pedido: "))

peso = payaso_peso * payasos + muñeca_peso * muñecas
if peso > 1000:
    num_kg = peso % 1000
    peso = peso - (num_kg*1000)
    peso = peso / 1000
    peso += num_kg
    print(f"EL peso del paquete es {peso:.2f}kg")
else:
    print(f"EL peso del paquete es {peso}g")
print("\n\n")


#Ejercicio 9
cantidad = int(input("Cual es la cantidad a inverir? "))
interes_anual  = int(input("Cual es el interes anual? "))
años = int(input("Cual es el numero de años a invertir? "))

interes_anual /= 100
interes = interes_anual * años * cantidad

print(f"Las ganacias producidas son {interes}, el capita total será {interes+cantidad}")
print("\n\n")


#Ejercicio 8
dividendo = int(input ("Ingrese un dividendo: "))
divisor = int(input ("Ingrese un divisor: "))

cociente = dividendo // divisor
residuo = dividendo % divisor
print(f"La division entre {dividendo} y {divisor} da un cociente {cociente} y un residuo de {residuo}")
print("\n\n")


#Ejercicio 7
kg = int(input("INgrese su peso en kg: "))
altura = int(input("Ingrese su altura en metros: "))
indice_masa_corporal = kg/altura**2
print(f"Su indice de masa cororal es , {indice_masa_corporal:.2f}")
print("\n\n")


#Ejercicio 6
n = int(input("Ingrese un numero hasta donde desea hacer la suma: "))
suma = (n*(n+1))/2
print(f"La suma de los positivos enteros hasta {n} es {suma}")
print("\n\n")


#Ejercicio 5
horas = int(input("Cuantas horas trabajo: "))
coste = int(input("Cuanto cuesta cada hora: "))
print(f"Usted ganó : {horas*coste}")
print("\n\n")



#Ejercicio 4
result = ((3+2)/(2.5))**2
print("((3+2)/(2.5))**2 = ",result)
print("\n\n")


#Ejercicio 3
variable = input("Type your name: ")
print(f"Hi {variable}")
print("\n\n")



#Ejercicio 2
variable = input("Type a string: ")
print(variable)
print("\n\n")



#Ejercicio 1
print("Hola MUndo")
print("\n\n")


