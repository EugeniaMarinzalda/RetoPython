print("Hola Mundo!")
# Variables - No poden variables cortas como x,y,z para que sea mas entendible. 
#Descriptivas, claras, mas de 2 caracteres. No existen constantes

# Tipo de datos - Las define python, es más rápido para codear. Pueden haber errores al cambiar de tipo

#nombre_de_la_variable = valor   snap case
first_name = "Eugenia" #String "" or ''
last_name = "Marinzalda"

#print(first_name)
#print(last_name)

full_name= first_name +" "+ last_name
#print(full_name)
#print(first_name +" "+ last_name)

age = 30 #int
score = 7.8 #float
active = True #bool

result = type(age)
#print(result)

#Para constantes indicar en mayus
VERSION= 3.11
#print(VERSION)

#Solicitar datos
#print("Ingrese su nombre")
#result=input()
#print("Se ingreso por teclado: " +result)

#result=input("Ingresa tu nombre: ") #En el mismo renglon
#print("Se ingreso por teclado: " +result)

#first_name= input("Ingresa tu nombre: ")
#age= input("Ingresa tu edad: ")
#score= input("Ingresa tu calificacion: ")
#active= input("El usuario se encuentra activo?: ")

#age=int(age)
#score=float(score)
#No recomendable, lo ideal es que la variable empiece y termine del mismo tipo

#print(first_name)
#print(float(age)) #No modifica la variable
#print(type(age)) 
#print(score)
#print(active)
#print (first_name, age, score, active)
#print (type(first_name), type(age), type(score), type(active))

#first_name= input("Ingresa tu nombre: ")
#age= int(input("Ingresa tu edad: "))
#score= float(input("Ingresa tu calificacion: "))
#active= input("El usuario se encuentra activo?: (si/no) ") == "si"

#print (first_name, age, score, active)
#print (type(first_name), type(age), type(score), type(active))

#operadores relacionales (==, !=, > , >=, <, <=)
#funciones: print - input - int - float - str

#reto: programa de registro de usuario
#Requisitos: Nombre, Apellido, telefono y correo electronico. Bienvenida  Hola + Nombre completo + Correo

print("Bienvenido al Reto Python")
print("A continuación, solicitaremos tus datos de registro")

first_name = str( input ("Ingresa tu/s nombre/s: "))
last_name  = str( input ("Ingresa tu apellido: "))
full_name= first_name + " " + last_name
telephone  = int( input ("Ingresa tu numero de telefono: "))
e_mail     = str( input ("Ingresa tu correo electronico: "))

print("Hola " + full_name + ", en breve recibirás un correo a " + e_mail)
