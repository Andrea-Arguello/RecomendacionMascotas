# -*- coding: cp1252 -*-
# Posible ejemplificacion de algortimo de recomendacion
# Maria Fernanda Lopez, Ana Lucia Hernandez, Andrea Arguello
# proyecto #2 - Estructura de datos
#5/05/2018


from hdt10 import *

ciclo = 0


while(ciclo==0):
    
    print ('\nQue desea hacer? \n>>1. ')

    entrada= raw_input(">>")
    print "\n**Usted ingreso: ", entrada,"**\n"



    if(entrada=="1"):
        name = raw_input("Ingrese el nombre del doctor: ")
        tel = raw_input("Ingrese el numero de contacto: ")
        col = raw_input("Ingrese el numero de colegiado: ")
        esp = raw_input("Ingrese la especialidad: ")
        add_Doctor(name,tel,col,esp)
        print '**Doctor ingresado**\n'
        ciclo = 0
    elif(entrada=="2"):
        name = raw_input("Ingrese el nombre del paciente: ")
        tel = raw_input("Ingrese el numero de contacto: ")
        add_Paciente(name,tel)
        print '**Paciente ingresado**\n'
        ciclo = 0
    elif(entrada=="3"):
        doctor = raw_input("Ingrese el nombre del doctor visitado: ")
        paciente = raw_input("Ingrese el nombre del paciente: ")
        fecha = raw_input("Ingrese la fecha de la visita: ")
        medicina = raw_input("Ingrese la medicina recetada: ")
        desde = raw_input("La tomara desde: ")
        hasta = raw_input("La tomara hasta: ")
        dosis = raw_input("Ingrese la dosis a tomar: ")
        registrarVisita(paciente,doctor,fecha,medicina,desde,hasta,dosis)
               
        ciclo = 0
    elif(entrada=="4"):
        esp = raw_input("Ingrese la especialidad que desea buscar: ")
        listaDocs = queryEsp(esp)
        print("\nDOCTORES QUE TIENEN LA ESPECIALIDAD DE "+esp.upper())
        for i in listaDocs:
            print("--> "+i)
        ciclo = 0
    elif(entrada=="5"):
        newciclo=0
        while (newciclo==0):
            opcion=raw_input("Son las personas:\n>>1. Doctor y Doctor\n>>2. Paciente y paciente\n>>")
            if(opcion!="1" and opcion!="2" and opcion!="3"):
                print "Ingrese una opcion valida"
                newciclo=0
            else:
                if(opcion=="1"):
                    persona1 = raw_input("Ingrese el primer doctor a relacionar: ")
                    persona2 = raw_input("Ingrese el segundo doctor a relacionar: ")
                    relacionDD(persona1,persona2)
                    newciclo=1
                    ciclo = 0
                elif(opcion=="2"):
                    persona1 = raw_input("Ingrese el primer paciente a relacionar: ")
                    persona2 = raw_input("Ingrese el segundo paciente a relacionar: ")
                    relacionPP(persona1,persona2)
                    newciclo=1
                    ciclo = 0
    elif(entrada=="6"):
        esp = raw_input("Ingrese la especialidad que desea buscar: ")
        doc = raw_input("Ingrese el nombre del doctor que desea le haga la recomendacion: ")
        recomendacionConocidosDoctor(esp, doc)
        ciclo = 0
    elif(entrada=="7"):
        esp = raw_input("Ingrese la especialidad que desea buscar: ")
        pac = raw_input("Ingrese el nombre del paciente que desea le haga la recomendacion: ")
        recomendacionConocidosPaciente(pac, esp)
        ciclo = 0
    elif(entrada=="8"):
        print "Feliz dia"
        ciclo = 1
    else:
        print "Ingrese una opcion valida\n"
        ciclo = 0

    
        
        
        

