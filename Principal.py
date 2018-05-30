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

            tenido=raw_input("Usted ha tenido alguna mascota anteriormente? (Seleccione solo una opcion):\n1. Gatos \t2. Perros \t3. Aves \n4. Roedores \t5. Reptiles \t6. Conejos \n7. Tarantulas \t8. Peces \t9. Hurones \n10. Cerditos (mini piggies) \t11. No he tenido mascotas \n>")
            while not (tenido=="1" or tenido=="2" or tenido=="3" or tenido=="4" or tenido=="5" or tenido=="6" or tenido=="7"  or tenido=="8" or tenido=="9"  or tenido=="10" or tenido=="11"):
                tenido=raw_input("Ingrese una opcion valida")
            if(tenido=="1"):
                tenidoin="Gato"
            elif(tenido=="2"):
                tenidop=raw_input("Que tipo de perro? (seleccione solo una opcion):\n1. Grande\t2. Mediano \t3. Pequenio")
                while not(tenidop=="1" or tenidop=="2" or tenidop=="3"):
                    tenidop=raw_input("Ingrese una opcion valida para el tamanio de perro: \n1. Grande\t2. Mediano \t3. Pequenio")
                if(tenidop=="1"):
                    tenidoin="Perro grande"
                elif(tenidop=="2"):
                    tenidoin="Perro mediano"
                elif(tenidop=="3"):
                    tenidoin=="Perro pequeno"
            elif(tenido=="3"):
                tenidoa=raw_input("Cual de las siguientes aves ha tenido? (Seleccione solo una opcion): \n1. Pericos \t2. Loros \t3.Canarios \n4. Cotorras \t5. Pollos \t6. Agapornis (love birds)\n>")
                while not(tenidoa=="1" or tenidoa=="2" or tenidoa=="3" or tenidoa=="4" or tenidoa=="5" or tenidoa=="6"):
                    tenidoa=raw_input("Ingrese una opcion valida (de 1 a 6)\n>")
                if(tenidoa=="1"):
                    tenidoin="Perico"
                elif(tenidoa=="2"):
                    tenidoin="Loro"
                elif(tenidoa=="3"):
                    tenidoin="Canarios"
                elif(tenidoa=="4"):
                    tenidoin="Cotorras"
                elif(tenidoa=="5"):
                    tenidoin="Pollos"
                elif(tenidoa=="6"):
                    tenidoin="Agapornis"
            elif(tenido=="4"):
                tenidor=raw_input("Cual de los siguientes roedores ha tenido? (Seleccione solo una opcion): \n1. Hamsters \t2. Ratones \t3. Cuyos\n>")
                while not(tenidor=="1" or tenidor=="2" or tenidor=="3"):
                    tenidor=raw_input("Ingrese una opcion valida (de 1 a 3)\n>")
                if(tenidor=="1"):
                    tenidoin="Hamster"
                elif(tenidor=="2"):
                    tenidoin="Ratones"
                elif(tenidor=="3"):
                    tenidoin="Cuyos"
            elif(tenido=="5"):
                tenidos=raw_input("Cual de los siguientes reptiles ha tenido? (Seleccione solo una opcion): \n1. Tortugas \t2. Serpientes \n3. Lagartos \t4. Lagartijas\n>")
                while not(tenidos=="1" or tenidos=="2" or tenidos=="3" or tenidos=="4"):
                    tenidos=raw_input("Ingrese una opcion valida (de 1 a 4)\n>")
                if(tenidos=="1"):
                    tenidoin="Tortuga"
                elif(tenidos=="2"):
                    tenidoin="Serpiente"
                elif(tenidos=="3"):
                    tenidoin="Lagartos"
                elif(tenidos=="4"):
                    tenidoin="Lagartijas"
            elif(tenido=="6"):
                tenidoin=="Conejos"
            elif(tenido=="7"):
                tenidoin=="Tarantula"
            elif(tenido=="8"):
                tenidoin="Pez"
            elif(tenido=="9"):
                tenidoin="Urones"
            elif(tenido=="10"):
                tenidoin="Mini piggies"
            elif(tenido=="11"):
                 tenidoin="" #Le puse espacio porque no se que mas podria ponerle
                    
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

            user=add_usuario(name,tenidoin,espacio,ninos,tiempo,personalidad,tipo,presupuesto,alergia)
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

        
            
            
            

