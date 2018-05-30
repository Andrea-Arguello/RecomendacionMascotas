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
            tenido=raw_input("Usted ha tenido una de las siguientes?:\n1.\n>")
            espacio=raw_input("El espacio con el cual cuenta en su casa es:\n1. Grande\n2. Moderado\n3. Pequenio\n>")
            ninos=raw_input("En su casa hay ninos pequenios?\n1. Si\n2. No\n>")
            tiempo=raw_input("Cuanto tiempo semanal podria invertir en su mascota?\n1. \n>")
            personalidad=raw_input("Usted considera que su personalidad es: \n1.'n>")
            tipo=raw_input("")
            presupuesto=raw_input("Usted cuenta con un presupuesto semanal para invertir en su mascota de:\n1. \n2. \3. \n>")
            alergia=("Usted tiene algun tipo de alergia?\n1. \n2. \n>")
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

        
            
            
            

