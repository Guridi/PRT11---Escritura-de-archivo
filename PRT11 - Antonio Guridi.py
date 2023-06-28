#Antonio Guridi 
#23-0638

"""
Desarrolle un programa que escriba un archivo CSV llamado 'clientes.csv', cuyo contenido 
se basará en la lista de diccionarios proporcionada a continuación 
(NO MODIFICAR LA LISTA, SÓLO COPIAR Y PEGAR EN SU CÓDIGO):
"""
#Librerias usadas
import  os #para poder manejar la consola desde codigo
from random import randint #Para obtener un numero aleatorio

Clientes = [

        {

            "Cedula": "001-1234542-6",

            "Nombre": "Angela",

            "Apellido": "Zapata",

            "FechaNacimiento": "1985-01-01"

        },

        {

            "Cedula": "402-7425963-8",

            "Nombre": "Juan",

            "Apellido": "Perez",

            "FechaNacimiento": "1992-05-12"

        },

        {

            "Cedula": "402-5236741-3",

            "Nombre": "Minerva",

            "Apellido": "Ramos",

            "FechaNacimiento": "1950-03-21"

        },

        {

            "Cedula": "001-6974235-2",

            "Nombre": "Roberto",

            "Apellido": "Matos",

            "FechaNacimiento": "1986-12-01"

        },

        {

            "Cedula": "001-8563217-9",

            "Nombre": "Silvestre",

            "Apellido": "Beras",

            "FechaNacimiento": "1998-04-02"

        }

    ]


with open('clientes.csv', 'w') as archivos: #Funcion para abrir el archivo y escribir en el
   
   archivos.write("Cedula, IdCliente, Cliente, FechaNacimiento\n") #Creacion de las columnas
   
   #recoger el contenido del diccionario que tenga como key 'Cedula' y almacenarlo en una lista
   ced = [c['Cedula'] for c in Clientes] 
    
    #Almacenar el numero random desde 1001 hasta 1005 sin repetirse
   Id = []
   for b in range(100):
     id = randint(1001, 1005)
     if id not in Id:
       Id.append(id)

    #recoger el contenido del diccionario que tenga como key 'Nombre' 'Apellido' y almacenarlo en una lista
   Nom = [n['Nombre'] for n in Clientes]
   Ap = [a['Apellido'] for a in Clientes]

   ##recoger el contenido del diccionario que tenga como key 'FechaNacimiento' y almacenarlo en una lista
   Fe = [f['FechaNacimiento'] for f in Clientes]
     
   for i in range(len(Clientes)): #Bucle que recorre toda la lista
    
    #Escritura del contenido de cada celda 
    archivos.write(f"{ced[i]}, {Id[i]}, {Nom[i]} {Ap[i]}, {Fe[i]} \n")
   

