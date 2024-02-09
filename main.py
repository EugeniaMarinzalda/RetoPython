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
#--------Día N°4: Tuplas y Diccionarios--------
#Estructuras de datos: Permiten almacenar distintos tipos de datos. Duplas dentro de duplas o listas dentro de duplas
#Todos los elementos pueden accederse mediante indices
#Las listas son mutables (cambiar tamaño y modificar datos) y las duplas inmutables (misma longitus y sin modificacion)

settings = ("localhost", 3306, "root", "password", "database") #-> parentesis type tuple
# Indices         0       1       3        4            5           
"""
print( len(settings)) #tamaño
print( settings[2]) #Acceder a un valor por indice
sub_setting = settings[::-1] #generar otra dupla a partir de la primera
print( sub_setting)
#Son mas seguras para almacenar valores que no pretendemos cambiar, la lectura es mas rapida y facil acceder a un indice
#Son colecciones, se pueden iterar
for value in settings:
    print(value)
#Si se quiere desagregar, se deben generar una variable por elemento para utilizarlas
host = settings[0]
port = settings[1]
username = settings[2]
password = settings[3]
name = settings[4]

#desempaquetado de duplas
host,port, username,password, name = settings
print(host,port, username,password, name)

host,port, _,_, _ = settings #Los valores que tienen _ no se asignan a ninguna variable
print(host,port)
host,port, *_ = settings # *_ cubre hasta el final
print(host,port)
host, *_, password, name = settings #Los valores que tienen *_ no se contemplan y respeta la ubicacion de los finales
print(host,password, name )

#duplas dentro de duplas. No olvidar "," entre duplas. Error
tuples = (
    (1,2,3),
    (4,5,6),
    (7,8,9)
)
print(tuples)
for _tuple in tuples:
    print(_tuple)

for _tuple in tuples: # para descomponen los valores de cada tupla. Numero individuales
    for number in _tuple:    
        print(number)

for number1, number2, number3 in tuples: #Desempauqetado de duplas sabiendo la cantidad de cada elemento en dupla
    print(number1, number2, number3)        
"""
#Diccionarios : Almacen distintos tipos de datos (primitivos, tuplas y otros diccionarios)
#NO trabajan con indice, sino con llave y valor (mapas, json)
#type dict
# Llave != String - Llave = Objetos inmutables - solo lectura
"""
user = {
    #llave : valor,
    "name" : "cody",
    "age" : "10",
    "email" : "info@codigofacilito.com",
    "active" : True,
    10 : 3.4,   
    True : "verdadero", # True se almacena por 1 y False por 0
    (1, 2, 3) : "Tupla"
}

print(user)

print(user["name"]) # Se accede al valor a traves de la llave

#Si no existe la lleve, obtenemos error. Para solucionar
if "username" in user:
    print( user ["username"])
if "name" in user:
    print( user ["name"])

#Metodo get. Obtiene el valor de la llave si existe. Si no existe es none (null)
value = user.get("username")   
print(value) 
value = user.get("username", "La llave no existe")   
print(value) 
value = user.get("name")   
print(value) 

#Metodo keys. Para conocer todas las llaves
print(
    user.keys()  #dict_keys
) 

print(
    list( user.keys() ) #Pasar a lista o tupla para trabajar 
)
#Metodo values. Para conocer todos los valores
print(
    user.values() #dict_values
)
print(
    tuple( user.values() ) #Pasar a lista o tupla para trabajar 
)
#Metodo items. Devuelve un objeto dict_item, donde se encuentra en duplas de 2 valores la llave y el valor
print(
    user.items() #dict_items
)
print(
    tuple( user.items() ) #Pasar a lista o tupla para trabajar 
)
# Se puede desagregar, desempaquetar
for key, value in tuple (user.items()):
    print(key, value)
"""
print("Bienvenido al Reto Python avance Día 4")
"""
Consignas:

Día 1: 

    Para este primer reto de la semana, tu objetivo será poder crear un programa en Python el cual permita registrar a un usuario en el sistema.

    Para ello el programa deberá pedir a nuestro usuario final ingrese su siguiente información.

    Nombre(s)
    Apellidos
    Número de teléfono
    Correo electrónico.
    Una vez el usuario haya ingresado todos los datos vía teclado, el programa le dará la bienvenida al usuario con el siguiente mensaje:

    Hola + seguido del nombre completo del usuario +, en breve recibirás un correo a + seguido del correo electrónico .

Día 2: 

    Para este segundo reto de la semana tu objetivo será incrementar el funcionamiento del programa del día de ayer. Si recordamos, ayer construimos un programa en Python capaz de registrar un nuevo usuario en el sistema. Pues bien, continuando con el proyecto, el reto de hoy será que podremos registrar un N cantidad de nuevos usuarios.

    Para esto el programa deberá preguntar cuando nuevos usuarios se pretenden registrar.

    Si el por ejemplo coloco 5, bueno, serán 5 nuevos usuarios los que se deben capturar, usuarios con sus correspondientes valores: Nombre, apellidos, número de teléfono y correo electrónico.

    Además de todo esto, añadiremos una capa extra de seguridad, implementando un par de validaciones sobre los valores que se pueden ingresar.

    Validaremos que, tanto nombre, apellidos como correo electrónico tengan una longitud mínimo de 5 caracteres y un longitud máxima de 50.

    Así mismo el número de teléfono será a 10 dígitos.

    Si por alguna razón el usuario ingresa mal alguno de estos datos, el programa deberá notificarle y no permitirá continuar hasta que se ingresen datos correctos.

Día 3: 

    Vaya, ya llegamos al reto número 3 de la semana, y para este tercer reto lo que haremos será añadir 2 nuevas funcionalidades a nuestro programa de registro de usuarios.

    Estas funcionalidades son las siguientes

    1.- Siempre que se registre un nuevo usuario de forma exitosa generaremos un identificador único para este registro/usuario. Te recomiendo sea un ID numérico auto incremental, que comience en 1 hasta N. Sin embargo siéntete libre elegir el formato o tipo que tú desees.
    2.- Todos estos nuevos identificadores deberán almacenarse en un listado que será impreso en consola cuando todos los registros se hayan creado. Esto de tal forma que el usuario pueda conocer y tenga certeza que las operaciones, en efecto, se realizaron de forma exitosa.

    Con estas 2 nuevas funcionalidades es probable te intuyas como iremos finalizando nuestro programa para el quinto día.

Día 4: 

    Ya nos encontramos en la recta final de nuestra semana, y lo que haremos ahora, cómo ya es costumbre, será añadir más funcionalidades a nuestro programa.

    Puntualmente 4 nuevas funcionalidades. Aquí van.

    1.- Ahora todos los valores que representan a un usuario: Nombre, apellidos, número de teléfono y correo electrónico deberán almacenarse en un diccionario.

    2.- Se añadirá la opción de poder listar el ID de todos los usuarios registrados hasta el momento.

    3.- Se añadirá la opción de poder ver la información de un usuario con respecto a un ID. Es decir, el usuario podrá ingresar un ID y a partir de este conocer la información registrada.

    4.- Se añadirá la opción de poder editar la información de un usuario con respecto a un ID. Es decir, el usuario podrá ingresar un ID y a partir de este el programa pedirá nuevamente los valores de un registro para actualizarlos.

    Estas 3 nuevas opciones deberán ser presentadas al usuario al comienzo del programa, esto con la finalidad que sea el usuario quien defina que quiere hacer justo ahora: añadir nuevos usuario, consultarlos o editarlos.

    De igual forma el programa tendrán una quinta opción que le permita la usuario finalizar el programa cuando él lo desee.

    Un Tip. Para estas nuevas opciones puedes presentarle a tu usuario un pequeño menú del cual pueda elegir. Por ejemplo opción A.-) registrar nuevos usuarios, opción B.-) listar usuarios, Opción C.-) Editar usuarios y así sucesivamente.

Día 5: 

    pass
"""
users = []
exit = False 
id=0  

"""
#Parametrizo 2 Usuarios para testear funcionamiento
user = {
                        "id" : 1,
                        "first_name" : "Holachau",
                        "last_name" : "apellido",
                        "telephone" : "1234567891",
                        "e_mail" : "correoelectronico"
                    }
users.append(user)
user = {
                        "id" : 2,
                        "first_name" : "comoestas",
                        "last_name" : "queeseso",
                        "telephone" : "1111122222",
                        "e_mail" : "electronico"
                    }
users.append(user)
id=2
"""
  
while exit == False:

    option = int ( input( "\nMenú "+
                          "\n   1 - Listar el ID de los usuarios registrados"+ 
                          "\n   2 - Agregar usuario/s"+ 
                          "\n   3 - Buscar usuario por ID"+ 
                          "\n   4 - Modificar usuario por ID"+ 
                          "\n   5 - Salir"+
                          "\n" ))
    
    # Controlo que el número ingresado este dentro del menú
    if option>5 or option<1:
        print("Opción incorrecta. Intente nuevamente")

    #Según la opción elegida
    match(option):

        case 1:
            #Listo únicamente los Id
            print("Los Id de los usuarios son: ")
            for user in users:
                print ("ID: ", user ["id"])

        case 2:
            flag = True #Para que salga del while si hay algún error en las validaciones
            number = 0

            registers = int(input("Cuantos registros deseas agregar?: "))

            while registers > 0 and flag == True:
                print( "Datos del nuevo registro")
                
                first_name = str( input ("Ingresa tu/s nombre/s: ")) 

                #Validación de nombres
                for character in first_name:
                    number += 1
                
                if number > 50 or number < 5:
                    print("Lo siento. La cantidad de caracteres para el nombre no es válida (min:5, max:50). Inicia nuevamente")
                    flag = False
                else:
                    number=0

                if flag == True:
                    last_name  = str( input ("Ingresa tu apellido: ")) 
                    
                    #Validación de apellido
                    for character in last_name:
                        number += 1
                
                    if number > 50 or number < 5:
                        print("Lo siento. La cantidad de caracteres para el apellido no es válida (min:5, max:50). Inicia nuevamente")
                        flag = False
                    else:
                        number=0

                if flag == True:
                    telephone  = int( input ("Ingresa tu número de teléfono: ")) 

                    #Validación de teléfono      
                    if telephone < 999999999 or telephone > 10000000000 :
                        print("Lo siento. El teléfono debe contener 10 dígitos. Inicia nuevamente")
                        flag = False
                        
                if flag == True:
                    e_mail = str( input ("Ingresa tu correo electrónico: ")) 
                    
                    #Validación de correo electrónico
                    for character in e_mail:
                        number += 1
                
                    if number > 50 or number < 5:
                        print("Lo siento. La cantidad de caracteres para el correo no es válida (min:5, max:50). Inicia nuevamente")
                        flag = False
                    else:
                        number=0
                
                #Si todos los pasos son correctos. Genero id, agrego las variables al diccionario y agrego el diccionario a la lista.
                if flag == True:
                    id += 1
                    print("Usuario registrado satisfactoriamente bajo el identificador: " , id)
                    user = {
                        "id" : id,
                        "first_name" : first_name,
                        "last_name" : last_name,
                        "telephone" : telephone,
                        "e_mail" : e_mail
                    } 
                    users.append(user)     
                registers -= 1 #Disminuyo los registros para que salga del bucle cuando cargue los usuarios

        case 3:
            flag = False
            search_id = int ( input ("Indique el ID del usuario que desea buscar: "))
            for user in users:
                if user ["id"] == search_id:
                    flag = True
                    print( "El usuario es: ")
                    for key, value in tuple (user.items()):
                        print(key, value)                
            if flag == False:
                print( "Id no encontrado. Intente nuevamente")

        case 4:
            banner = False #Para controlar que el usuario se haya encontrado
            number = 0
            id_change = int ( input ("Indique el ID del usuario que desea modificar: "))
            for user in users:
                if user ["id"] == id_change:
                    banner = True
                    flag = True
                    print( "El usuario a modificar es: ")
                    for key, value in tuple (user.items()):
                        print(key, value) 

                    while flag == True:

                        first_name = str( input ("Ingresa tu/s nombre/s: ")) 

                        #Validación de nombres
                        for character in first_name:
                            number += 1
                        
                        if number > 50 or number < 5:
                            print("Lo siento. La cantidad de caracteres para el nombre no es válida (min:5, max:50). Inicia nuevamente")
                            flag = False
                        else:
                            number=0

                        if flag == True:
                            last_name  = str( input ("Ingresa tu apellido: ")) 
                            
                            #Validación de apellido
                            for character in last_name:
                                number += 1
                        
                            if number > 50 or number < 5:
                                print("Lo siento. La cantidad de caracteres para el apellido no es válida (min:5, max:50). Inicia nuevamente")
                                flag = False
                            else:
                                number=0

                        if flag == True:
                            telephone  = int( input ("Ingresa tu número de teléfono: ")) 

                            #Validación de teléfono      
                            if telephone < 999999999 or telephone > 10000000000 :
                                print("Lo siento. El teléfono debe contener 10 dígitos. Inicia nuevamente")
                                flag = False
                                
                        if flag == True:
                            e_mail = str( input ("Ingresa tu correo electrónico: ")) 
                            
                            #Validación de correo electrónico
                            for character in e_mail:
                                number += 1
                        
                            if number > 50 or number < 5:
                                print("Lo siento. La cantidad de caracteres para el correo no es válida (min:5, max:50). Inicia nuevamente")
                                flag = False
                            else:
                                number=0
                        
                        #Si todos los pasos son correctos. Agrego las variables a un nuevo diccionario.
                        if flag == True:
                
                            new_user = {
                                "id" : id_change,
                                "first_name" : first_name,
                                "last_name" : last_name,
                                "telephone" : telephone,
                                "e_mail" : e_mail
                            } 
                            #Lo inserto en la posición del usuario a modificar, este se desplaza en una posición.
                            users.insert((id_change-1),new_user)
                            #Elimino el usuario anterior que se desplazo
                            users.remove(user) 
                            flag= False

            if banner == False:
                print( "Id no encontrado. Intente nuevamente")

        case 5:
            exit = True
