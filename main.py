#Dia N°1
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


#funciones: print - input - int - float - str

#reto: programa de registro de usuario
#Requisitos: Nombre, Apellido, telefono y correo electronico. Bienvenida  Hola + Nombre completo + Correo
""" 
print("Bienvenido al Reto Python")
print("A continuación, solicitaremos tus datos de registro")

first_name = str( input ("Ingresa tu/s nombre/s: "))
last_name  = str( input ("Ingresa tu apellido: "))
full_name= first_name + " " + last_name
telephone  = int( input ("Ingresa tu numero de telefono: "))
e_mail     = str( input ("Ingresa tu correo electronico: "))

print("Hola " + full_name + ", en breve recibirás un correo a " + e_mail)
"""

#Día N°2: Estructuras de control
# if, match (swich), foreach, while

#Bool True False
#Operadores logicos (and, or, not)
#operadores relacionales (==, !=, > , >=, <, <=)

"""
number1=10
number2=20
result = number1 < number2 and 10 == 10
print(result)
print(not result)
pass palabra reservada para indicar que esta vacio

#Estructura
if <condition (True/False)>:
    pass

if True:
    print("La condicion es True")

if 10>20:
    print("La condicion se cumple")
else:
    print("La condicion no se cumple")

age = int(input ('Ingresa tu edad: '))

if age>=0 and age<=110:
    if age>=18:
        print("Tienes la edad para votar")
    else:
        print("No tienes la edad para votar")    
else:
    print("La edad no es valida, intenta de nuevo (min:0, max:110)")     

#elif

color="green"
if color == "green":
    print("Puede continuar")
elif color == "yellow":
    print("alto parcial")    
elif color == "red":
    print("Alto total")
else:        
    print("El color no es valido")

#swich
color="grey"  
match color:
    case "red":    
        print("Alto total")
    case "yellow":    
        print("Alto parcial")
    case "green":    
        print("Puede continuar")
    case _:
        print("Lo sentimos, el codigo no es valido")    

#Ciclos
#foreach -> cuando sepamos cuantas iteracciones se necesitan
#while -> cuando no sepamos cuantas iteracciones se necesitan (Condición)

title = "Estructuras de control"
for caracter in title:
    print(caracter)

for number in range(1,101): # el 101 no se incluye
    if not number % 2 == 0:
        print(number)

while <condition>:
    pass

number = 0
while number < 10: #No es el correcto porque se sabe de antemano cuantas iteracciones existen
    print(number)
    number += 1
else:
    print("La condicion no se cumple")

#random = 5
#number = 0
#max_attends = 5
random, number, max_attends = 5, 0, 5

while number != random and max_attends >= 1: #Correcto No sabe cuantos intentos
    number = int ( input("Ingresa un número: "))
    max_attends -= 1
else:
    if number == random:
        print("Felicidades, encontraste el número" )    
    else:
        print ("Lo sentimos, te quedaste sin intentos")


print("Bienvenido al Reto Python avance Día 2")

registers = int(input("Cuantos registros deseas agregar?: "))
flat = True
number = 0
while registers > 0 and flat == True:
    print("Datos del nuevo registro")
    
    first_name = str( input ("Ingresa tu/s nombre/s: ")) #longitud mínimo de 5 caracteres y un longitud máxima de 50
    
    for character in first_name:
        number += 1
      
    if number > 50 or number < 5:
        print("Lo siento. La cantidad de caracteres para el nombre no es válida (min:5, max:50). Inicia nuevamente")
        flat = False
    else:
        number=0

    if flat == True:
        last_name  = str( input ("Ingresa tu apellido: "))  #longitud mínimo de 5 caracteres y un longitud máxima de 50
        
        for character in last_name:
            number += 1
      
        if number > 50 or number < 5:
            print("Lo siento. La cantidad de caracteres para el apellido no es válida (min:5, max:50). Inicia nuevamente")
            flat = False
        else:
            number=0

    full_name= first_name + " " + last_name

    if flat == True:
        telephone  = int( input ("Ingresa tu número de teléfono: ")) #el número de teléfono será a 10 dígitos
              
        if telephone < 999999999 or telephone > 10000000000 :
            print("Lo siento. El teléfono debe contener 10 dígitos. Inicia nuevamente")
            flat = False
            
    if flat == True:
        e_mail = str( input ("Ingresa tu correo electrónico: ")) #longitud mínimo de 5 caracteres y un longitud máxima de 50
        for character in e_mail:
            number += 1
      
        if number > 50 or number < 5:
            print("Lo siento. La cantidad de caracteres para el correo no es válida (min:5, max:50). Inicia nuevamente")
            flat = False
        else:
            number=0
    
    if flat == True:
        print("Registro cargado satisfactoriamente")        
    registers -= 1


#Si por alguna razón el usuario ingresa mal alguno de estos datos, el programa deberá notificarle y no permitirá continuar hasta que se ingresen datos correctos.
""" 

