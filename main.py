#--------Dia N°1--------
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

#--------Día N°2: Estructuras de control--------
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
# --------Día 3---------
# Listas = Estructuras de datos. Almacena distintos tipos de datos. type list. 
# Mutables: Modifican su indice y longitud
# Listas en plural, elemento en singular
"""

my_list = ["dato1" , "dato2"] #-> Estructura
#    indice    0          1         total = 2

print(len(my_list))
last_index = len (my_list)-1
print(my_list[last_index])
"""
courses = ["Python", "Django", "Flask", "Ruby", "Ruby on Rails", "Rust" , "C#"]
#            0          1         2        3            4          5        6
#           -7         -6        -5       -4           -3         -2       -1
"""
last_index = len (courses)-1
index = int( input("Ingresa el indice del cual quieres conocer su valor: "))

if index <= last_index:
    print ( courses[index])
else:
    print("Lo sentimos, el indice no es valido")    

#Generar sublistas
new_list = courses [0:5]   # [incluye:excluye]
print(new_list)
new_list = courses [3:]   # [incluye:ultimo]
print(new_list)
new_list = courses [:5]   # [primero:excluye]
print(new_list)

#Generar sublistas con saltos
new_list = courses [::2]   # De dos en dos
#new_list = courses [star:stop:skips]   # Estructura
print(new_list)
new_list = courses [::-1]   # Lista a la inversa
print(new_list)

#Metodos o acciones que la lista puede realizar
# append, insert, remove, clear, count, index

#append: añade un elemento al final de la lista.
courses.append("JavaScript")
courses.append("TypeScript")
courses.append("Swift")

#print(courses)
#print(courses[-1])
#print( len(courses))

courses.insert(1,"SQLServer")   #inserta desplazando hacia la derecha. ojo
#print(courses)

#extend : toma una lista y la agrega al final de otra lista. Sirve mejor que iterar y agregar
new_courses = ["Java9","Docker","Unix"]
courses.extend(new_courses)
print(courses)

#remove : elimina
courses.remove ("Python")
courses.remove ("Flask")
courses.remove ("C#")
print(courses)

#Count : Cuantas veces aparece ese elemento en la lista
print( courses.count("Python"))
print( courses.count("Unix"))

#in : Para saber si un elemento se encuentra en la lista (True/False)
print( "Ruby" in courses)
print( "Laravel" in courses)

#index : Para conocer el indice de un elemento
print( courses.index("Ruby"))
#print( courses.index("Laravel")) #-> si no existe sale error
#Para solucionarlo
value = "Laravel"
if value in courses:
    print("El indice es: " + str( courses.index(value)))
else:
    print("Lo sentimos, el valor no existe dentro del listado") 

value = "Java9"
if value in courses:
    print("El indice es: " + str( courses.index(value)))
else:
    print("Lo sentimos, el valor no existe dentro del listado")    

#clear: limpia la lista completa
#courses.clear()
#print(courses)

#foreach
for course in courses:
    print(course)

#para saber el indice se utiliza enumerate. Recibe una lista o str y se puede saber el indice
for index,course in enumerate(courses):
    print("El valor para el indice ", index, " " ,course)

for index,character in enumerate("Hola Mundo"): #inlcuye espacio. Los str son coleccion de caracteres NO mutables
    print(index, character)

# los metodos se pueden utilizar para generar un nuevo str
message = "Hola Mundo"
new_messaje = "P" + message[1:]
print(new_messaje)        

print("Bienvenido al Reto Python avance Día 3")
flat = True
number = 0
id=0
users = []

registers = int(input("Cuantos registros deseas agregar?: "))

while registers > 0 and flat == True:
    print("Datos del nuevo registro")
    
    first_name = str( input ("Ingresa tu/s nombre/s: ")) 

    for character in first_name:
        number += 1
      
    if number > 50 or number < 5:
        print("Lo siento. La cantidad de caracteres para el nombre no es válida (min:5, max:50). Inicia nuevamente")
        flat = False
    else:
        number=0

    if flat == True:
        last_name  = str( input ("Ingresa tu apellido: ")) 
        
        for character in last_name:
            number += 1
      
        if number > 50 or number < 5:
            print("Lo siento. La cantidad de caracteres para el apellido no es válida (min:5, max:50). Inicia nuevamente")
            flat = False
        else:
            number=0

    full_name= first_name + " " + last_name

    if flat == True:
        telephone  = int( input ("Ingresa tu número de teléfono: ")) 
              
        if telephone < 999999999 or telephone > 10000000000 :
            print("Lo siento. El teléfono debe contener 10 dígitos. Inicia nuevamente")
            flat = False
            
    if flat == True:
        e_mail = str( input ("Ingresa tu correo electrónico: ")) 
        for character in e_mail:
            number += 1
      
        if number > 50 or number < 5:
            print("Lo siento. La cantidad de caracteres para el correo no es válida (min:5, max:50). Inicia nuevamente")
            flat = False
        else:
            number=0
    
    if flat == True:
        id += 1
        print("Usuario registrado satisfactoriamente bajo el identificador: " , id)
        users.append(id)        
    registers -= 1

if len(users)>0:
    print("Los identificadores de los usuarios registrados son: ")
    for user in users:
        print(user)    
else:
    print("No hay usuarios registrados")        
"""    