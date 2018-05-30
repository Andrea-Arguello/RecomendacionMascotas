# -*- coding: cp1252 -*-
# Posible ejemplificacion de algortimo de recomendacion
# Maria Fernanda Lopez, Ana Lucia Hernandez, Andrea Arguello
# proyecto #2 - Estructura de datos
#29/05/2018


from modulo import *

ciclo = 0


while(ciclo==0):
    if dbVacia():
        #Se crea una base de datos en dado caso se inicie por primera vez
        print ('\nEspere mientras se genera la base de datos...')
        add_espacio()
        add_ninos()
        add_personalidad()
        add_alergia()
        add_tiempo()
        add_tipoM()
        add_presu()
        add_preusuarios()
        add_animal() 
        print ('\nBase de datos generada')
        
    else:
        print ('\nQue desea hacer? \n**1. Buscar mi mascota ideal \n**2. Buscar mascotas por caracteristicas \n**3. Buscar por conocido\n**4. Salir')

        entrada= raw_input(">>")
        print "\n**Usted ingreso: ", entrada,"**\n"


        if(entrada=="1"):
            print "Responda a las siguientes preguntas de la manera mas honesta posible:"
            name = raw_input("Ingrese su nombre: ")
            tenido=raw_input("Usted ha tenido una de las siguientes?:\n1.\n>") #HACE FALTA
            
            espacio=raw_input("El espacio con el cual cuenta en su casa es:\n1. Pequenio\n2. Grande\n3. Moderado\n>")
            while not(espacio=="1" or espacio=="2" or espacio=="3"):
                espacio=raw_input("Ingrese una opcion valida:\n1. Pequenio\n2. Grande\n3. Moderado\n>")
            
            ninos=raw_input("En su casa hay ninos pequenios?\n1. No\n2. Si\n>")
            while not(ninos=="1" or ninos=="2"):
                ninos=raw_input("Ingrese una opcion valida\nEn su casa hay ninos pequenios?\n1. No\n2. Si\n>")
            ninos-- #lo coloca en 0 si es no y 1 si es si

            tiempo=raw_input("Cuanto tiempo (en horas) semanal podria invertir en su mascota?\n1. 0-3\n2. 4-7\n3. 8-11\n>")
            while not(tiempo=="1" or tiempo=="2" or tiempo=="3"):
                tiempo=raw_input("Ingrese una opcion valida:\n1. 0-3\n2. 4-7\n3. 8-11\n>")
            tiempo-- #lo coloca en 0, 1 y 2 respectivamente

            personalidad=raw_input("Usted considera que su personalidad es: \n1. Introvertida\n2. Extrovertida\n>")
            while not(personalidad=="1" or personalidad=="2"):
                personalidad=raw_input("Ingrese una opcion valida\nUsted considera que su personalidad es: \n1. Introvertida\n2. Extrovertida\n>")
            personalidad-- #lo coloca en 0 y 1

            tipo=raw_input("Desea una mascota que sea:\n1. No activa (tranquila)\n2. Activa\n>")
            while not(tipo=="1" or tipo=="2"):
                alergia=raw_input("Ingrese una opcion valida\nDesea una mascota que sea:\n1. No activa (tranquila)\n2. Activa\n>")
            tipo-- #lo coloca en 0 y 1

            presupuesto=raw_input("Usted cuenta con un presupuesto semanal para invertir en su mascota de:\n1. Poco presupuesto \n2. Presupuesto regular \3. Alto presupuesto\n>")
            while not(presupuesto=="1" or presupuesto=="2" or presupuesto=="3"):
                presupuesto=raw_input("Ingrese una opcion valida:\n1. Poco presupuesto \n2. Presupuesto regular \3. Alto presupuesto\n>")
            presupuesto-- #lo coloca en 0, 1 y 2 respectivamente

            alergia=("Usted tiene algun tipo de alergia?\n1. No\n2. Si\n>")
            while not(alergia=="1" or alergia=="2"):
                alergia=raw_input("Ingrese una opcion valida\nUsted tiene algun tipo de alergia?\n1. No\n2. Si\n>")
            alergia-- #lo coloca en 0 y 1

            user=add_usuario(name,tenido,espacio,ninos,tiempo,personalidad,tipo,presupuesto,alergia)
            print '**Su usuario ha sido ingresado. Espere mientras hallamos la mascota ideal para usted**\n'
            
            ciclo = 0
        elif(entrada=="2"):
            car = raw_input("Ingrese la caracteristica a buscar: ")
            tel = raw_input("Ingrese el numero de contacto: ")
            add_Paciente(name,tel)
            print 'Sus resultados son:'
            ciclo = 0
        elif(entrada=="3"):
            ciclo=0
        elif(entrada=="4"):
            print "Feliz dia"
            ciclo = 1
        else:
            print "Ingrese una opcion valida\n"
            ciclo = 0

        
            
            
            

