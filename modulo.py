# -*- coding: cp1252 -*-
# Posible ejemplificacion de algortimo de recomendacion
# Maria Fernanda Lopez, Ana Lucia Hernandez, Andrea Arguello
# proyecto #2 - Estructura de datos
#5/05/2018


from neo4jrestclient.client import GraphDatabase
from neo4jrestclient import client
import openpyxl
import sys
import collections


driver = GraphDatabase("http://localhost:7474", username="neo4j", password="mypassword")

rangoPresuV = ["0", "1", "2"]
rangoPresu = ["Poco presupuesto", "Regular presupuesto", "Alto presupuesto"]
rangoEspacioV = ["1", "2", "3"]
rangoEspacio = ["Pequeno", "Moderado", "Grande"]
ninosPequesV = ["1","0"]
ninosPeques = ["Si", "No"]
hrSemanaV = ["0", "1", "2"]
hrSemana = ["0-3", "4-7", "8-11"]
personalidadV = ["1", "0"]
personalidad = ["Extrovertida", "Introvertida"]
tipoMases = ["Activo", "No activo"]
tipoMasesV = ["1", "0"]
alergias = ["Es alergico", "No es alergico"]
alergiasV = ["1", "0"]

usuario = driver.labels.create("Usuario")
animal = driver.labels.create("Animal")
tiempo = driver.labels.create("CaracteristicaTiempo")
espaciop = driver.labels.create("CaracteristicaEspacio")
presupuesto = driver.labels.create("CaracteristicaPresupuesto")
personalidades = driver.labels.create("CaracteristicaPersonalidad")
tipoMas = driver.labels.create("CaracteristicaTipoM")
ninos = driver.labels.create("CaracteristicaNinos")
alergia = driver.labels.create("CaracteristicaAlergia")


#------------------------------------------------------------------------------

#-------- CREACION NODOS POR DEFAULT EN EL GRAFO ---------

#para agregar los nodos del presupuestos
def add_presu():
    for i in range(len(rangoPresu)):
        pres = driver.nodes.create(Nombre=rangoPresu[i], Valor= rangoPresuV[i])
        presupuesto.add(pres)

#agregar un Si o un No para hacer las relaciones de si tiene niños pequeños
def add_ninos():
    for i in range(len(ninosPeques)):
        nn = driver.nodes.create(Nombre=ninosPeques[i], Valor= ninosPequesV[i])
        ninos.add(nn)

#Agregar nodos de rango de tiempo que le puede dedicar por semana
def add_tiempo():
    for i in range(len(hrSemana)):
        tt = driver.nodes.create(Nombre=hrSemana[i], Valor=hrSemanaV[i])
        tiempo.add(tt)

#agregar un Si o un No de si tiene alergia el usuario o si el animal genera  o no alergias
def add_personalidad():
    for i in range(len(personalidad)):
        pp = driver.nodes.create(Nombre=personalidad[i], Valor= personalidadV[i])    #seria bueno tal vez ponerle otro nombre pero la mera verdad no se me ocurre
        personalidades.add(pp)

#agregar un Si o un No de si tiene alergia el usuario o si el animal genera  o no alergias
def add_alergia():
    for i in range(len(alergias)):
        al = driver.nodes.create(Nombre=alergias[i], Valor= alergiasV[i])
        alergia.add(al)

#agregar un nodo de activo o inactivo para el tipo de mascota
def add_tipoM():
    for i in range(len(tipoMases)):
        tipo = driver.nodes.create(Nombre=tipoMases[i], Valor= tipoMasesV[i])
        tipoMas.add(tipo)


def add_espacio():
    for i in range(len(rangoEspacio)):
        space = driver.nodes.create(Nombre=rangoEspacio[i], Valor= rangoEspacioV[i])
        espaciop.add(space)
        
def add_preusuarios():
    #aqui se tendria que leer el archivo de texto de la base de datos de analu + el de la db de google
    archivo = open("users.txt", "r")  #esto es supositorio (el nombre)
    contenido = archivo.readlines()
    archivo.close()
    for lineas in contenido:
        users = lineas.split(", ")
        ul = driver.nodes.create(Nombre=users[0], Tenido=users[1], Espacio=users[2], Ninos=users[3], Tiempo=users[4], Personalidad=users[5], Tipo=users[6], Presupuesto=users[7], Alergia=users[8])
        usuario.add(ul)
        prefMas(users[0], users[6])
        relacionUA(users[0], users[8])
        relacionPresupuesto(users[0], users[7])
        espacio(users[0], users[2]) 
        relacionNinos(users[0], users[3])
        tiempoUser(users[0], users[4])
        personalidadUsuario(users[0], users[5]) 
        experiencia = users[1].split(" y ")
        for mascota in experiencia:
            haTenido(users[0], mascota)

def add_animal():
    archivo = open("animales.txt", "r")  
    contenido = archivo.readlines()
    archivo.close()
    for lineas in contenido:
        animales = lineas.split(", ")
        an = driver.nodes.create(Nombre=animales[0], Presupuesto=animales[1], Alergia=animales[2], Espacio=animales[3], Ninos=animales[4], Tiempo=animales[5], Personalidad=animales[6], Tipo=animales[7])
        animal.add(an)
        esMascota(animales[0], animales[7])
        relacionAA(animales[0], animales[2])
        presupuestoAni(animales[0], animales[1]) #experiencia
        espacioAni(animales[0], animales[3])
        amigable(animales[0], animales[4])
        tiempoAni(animales[0], animales[5])
        personalidadAni(animales[0], animales[6])

    

#-------------------------------------------------------------------------------------------
#----- CREACION DE NODOS EN TIEMPO DE EJECUCION ---------------------
    
def add_usuario(nombre, tenido, space, ninos, tiempo, personalidad, tipo, presupuesto, alergia):
    # tenido sera un array
    experiencia ="" #el array se traslada a un string que se guarda en el txt
    for i in tenido:
        if (len(tenido)!=1 or i != (tenido[len(tenido)-1])):
            experiencia += i + " y "
        else:
            experiencia += i
        
    u1 = driver.nodes.create(Nombre=nombre, Tenido=experiencia, Espacio=space, Ninos=ninos, Tiempo=tiempo, Personalidad=personalidad, Tipo=tipo, Presupuesto=presupuesto, Alergia=alergia)
    usuario.add(u1)
    prefMas(nombre, str(tipo))
    relacionUA(nombre, str(alergia))
    relacionPresupuesto(nombre, str(presupuesto))
    espacio(nombre, str(space))
    relacionNinos(nombre, str(ninos))
    tiempoUser(nombre, str(tiempo))
    personalidadUsuario(nombre, str(personalidad))
    for mascota in tenido:
        haTenido(nombre, mascota)
    archivo = open("users.txt", "a")
    archivo.write(nombre + ", " + experiencia + ", " + str(space) + ", " + str(ninos) + ", " + str(tiempo) + ", " + str(personalidad) + ", " + str(tipo) + ", " + str(presupuesto) + ", " + str(alergia)+ ", "+"\n")
    archivo.close()
    return u1



#---------------------------------------------------------------------------------------


#------ RELACIONES ANIMALES -----


def esMascota(animal, tipo):
    q = 'MATCH (u:Animal), (s:CaracteristicaTipoM) WHERE u.Nombre=\"'+ animal +'\" AND s.Valor=\"'+ tipo +'\" RETURN u,s'
    resultados = driver.query(q, returns=(client.Node, client.Node))
    for i in resultados:
        a = i[0]
        t = i[1]
        a.relationships.create("Es_una_mascota", t)


def relacionAA(animal, alergia):
    q = 'MATCH (u:Animal), (s:CaracteristicaAlergia) WHERE u.Nombre=\"'+ animal +'\" AND s.Valor=\"'+ alergia +'\" RETURN u,s'
    resultados = driver.query(q, returns=(client.Node, client.Node))
    for i in resultados:
        a = i[0]
        al = i[1]
        a.relationships.create("Puede_estar_con_alguien_que", al)

def presupuestoAni(animal, presupuesto):
    q = 'MATCH (u:Animal), (s:CaracteristicaPresupuesto) WHERE u.Nombre=\"'+ animal +'\" AND s.Valor=\"'+ presupuesto +'\" RETURN u,s'
    resultados = driver.query(q, returns=(client.Node, client.Node))
    for i in resultados:
        u = i[0]
        pre = i[1]
        u.relationships.create("Costo_mensual_de_manutencion", pre)

def espacioAni(animal, espacio):
    q = 'MATCH (u:Animal), (s:CaracteristicaEspacio) WHERE u.Nombre=\"'+ animal +'\" AND s.Valor=\"'+ espacio +'\" RETURN u,s'
    resultados = driver.query(q, returns=(client.Node, client.Node))
    for i in resultados:
        u = i[0]
        e = i[1]
        u.relationships.create("Cantidad_de_espacio_que_necesitan", e)

def amigable(animal, ninos):
    q = 'MATCH (u:Animal), (s:CaracteristicaNinos) WHERE u.Nombre=\"'+ animal +'\" AND s.Valor=\"'+ ninos +'\" RETURN u,s'
    resultados = driver.query(q, returns=(client.Node, client.Node))
    for i in resultados:
        u = i[0]
        ni = i[1]
        u.relationships.create("Pueden_estar_en_un_hogar_que", ni)

def tiempoAni(animal, tiempo):
    q = 'MATCH (u:Animal), (s:CaracteristicaTiempo) WHERE u.Nombre=\"'+ animal +'\" AND s.Valor=\"'+ tiempo +'\" RETURN u,s'
    resultados = driver.query(q, returns=(client.Node, client.Node))
    for i in resultados:
        u = i[0]
        pre = i[1]
        u.relationships.create("Cantidad_de_tiempo_que_necesitan", pre)

def personalidadAni(animal, personalidad):
    q = 'MATCH (u:Animal), (s:CaracteristicaPersonalidad) WHERE u.Nombre=\"'+ animal +'\" AND s.Valor=\"'+ personalidad +'\" RETURN u,s'
    resultados = driver.query(q, returns=(client.Node, client.Node))
    for i in resultados:
        u = i[0]
        t = i[1]
        u.relationships.create("Recomendable_para_una_persona", t)
    

    
#----------------------------------------------------------------------------------------------------


#------ RELACIONES USUARIOS -----
def haTenido(usuario, animal):
    q = 'MATCH (u:Usuario), (s:Animal) WHERE u.Nombre=\"'+ usuario +'\" AND s.Nombre=\"'+ animal +'\" RETURN u,s'
    resultados = driver.query(q, returns=(client.Node, client.Node))
    for i in resultados:
        u = i[0]
        a = i[1]
        u.relationships.create("Ha_Tenido", a)
        
#no cree los nodos de "Espacio" porque como esos estan por default pensaba que los metieramos de una en neo4j de una con los atributos con este nombre
def espacio(usuario, espacio):
    q = 'MATCH (u:Usuario), (s:CaracteristicaEspacio) WHERE u.Nombre=\"'+ usuario +'\" AND s.Valor=\"'+ espacio +'\" RETURN u,s'
    resultados = driver.query(q, returns=(client.Node, client.Node))
    for i in resultados:
        u = i[0]
        e = i[1]
        u.relationships.create("Espacio_disponible", e)

#no cree los nodos de "TipoM" porque como esos estan por default pensaba que los metieramos de una en neo4j de una con los atributos con este nombre
def prefMas(usuario, tipo):
    q = 'MATCH (u:Usuario), (s:CaracteristicaTipoM) WHERE u.Nombre=\"'+ usuario +'\" AND s.Valor=\"'+ tipo +'\" RETURN u,s'
    resultados = driver.query(q, returns=(client.Node, client.Node))
    for i in resultados:
        u = i[0]
        t = i[1]
        u.relationships.create("Prefiere_una_mascota", t)

#no cree los nodos de "Presupuesto" porque como esos estan por default pensaba que los metieramos de una en neo4j de una con los atributos con este nombre
def relacionPresupuesto(usuario, presupuesto):
    q = 'MATCH (u:Usuario), (s:CaracteristicaPresupuesto) WHERE u.Nombre=\"'+ usuario +'\" AND s.Valor=\"'+ presupuesto +'\" RETURN u,s'
    resultados = driver.query(q, returns=(client.Node, client.Node))
    for i in resultados:
        a = i[0]
        pre = i[1]
        a.relationships.create("Tiene", pre)


#no cree los nodos de "Alergia" porque como esos estan por default pensaba que los metieramos de una en neo4j de una con los atributos con este nombre
def relacionUA(usuario, alergia):
    q = 'MATCH (u:Usuario), (s:CaracteristicaAlergia) WHERE u.Nombre=\"'+ usuario +'\" AND s.Valor=\"'+ alergia +'\" RETURN u,s'
    resultados = driver.query(q, returns=(client.Node, client.Node))
    for i in resultados:
        u = i[0]
        al = i[1]
        u.relationships.create("Tiene_alergia", al)

#no cree los nodos de "Ninos" porque como esos estan por default pensaba que los metieramos de una en neo4j de una con los atributos con este nombre
def relacionNinos(usuario, ninos):
    q = 'MATCH (u:Usuario), (s:CaracteristicaNinos) WHERE u.Nombre=\"'+ usuario +'\" AND s.Valor=\"'+ ninos +'\" RETURN u,s'
    resultados = driver.query(q, returns=(client.Node, client.Node))
    for i in resultados:
        u = i[0]
        ni = i[1]
        u.relationships.create("Tiene_ninos", ni)

def personalidadUsuario(usuario, personalidad):
    q = 'MATCH (u:Usuario), (s:CaracteristicaPersonalidad) WHERE u.Nombre=\"'+ usuario +'\" AND s.Valor=\"'+ personalidad +'\" RETURN u,s'
    resultados = driver.query(q, returns=(client.Node, client.Node))
    for i in resultados:
        u = i[0]
        t = i[1]
        u.relationships.create("Personalidad", t)
    

#Relacion para realizar el algoritmo de recomendacion hibrido
def relacionUU(usuario, usuario1):
    q='MATCH (u:Usuario) WHERE u.Nombre=\"'+ usuario1 +'\" RETURN u'
    doctores1 = driver.query(q,returns=(client.Node,str,client.Node))
    for p in doctores1:
        print("(%s)" % (p[0]["Nombre"]))
    p1=p[0]

    r='MATCH (u:Usuario) WHERE u.Nombre=\"'+ usuario +'\" RETURN u'
    doctores = driver.query(r,returns=(client.Node,str,client.Node))
    for r in doctores:
        print("(%s)" % (r[0]["Nombre"]))
    d1=r[0]
    d1.relationships.create("Conoce", p1)

def tiempoUser(usuario, tiempo):
    q = 'MATCH (u:Usuario), (s:CaracteristicaTiempo) WHERE u.Nombre=\"'+ usuario +'\" AND s.Valor=\"'+ tiempo +'\" RETURN u,s'
    resultados = driver.query(q, returns=(client.Node, client.Node))
    for i in resultados:
        u = i[0]
        pre = i[1]
        u.relationships.create("Tiempo_disponible", pre)


#-------------------------------------------------------------------------------------------------------------


# ------- QUERYS -----
def getConocidosUser(nombreUser):
    conocidosL=[]
    q = 'MATCH (u:Usuario)-[r:Conoce]->(m:Paciente) WHERE u.Nombre=\"'+ nombreUser +'\" RETURN u, type(r), m'
    conocidos = driver.query(q, returns=(client.Node, str, client.Node))
    if len(conocidos) ==0:
        print("\n-----> La persona que ingreso no tiene conocidos o no existe")
    else:
        for r in conocidos:
            conocidosL.append(r[2]["Nombre"])
        return conocidosL

def dbVacia():
    vacia=False
    q = 'MATCH (n) RETURN n'
    busqueda=driver.query(q, returns=(client.Node,client.Node))
    if len(busqueda)==0:
        vacia=True
    return vacia

#-------------------------------------------------------------------------------------------------------------
#----------- RECOMENDACIONES ---------------

def getMascotaR(nombre, tenido, space, ninos, tiempo, personalidad, tipo, presupuesto, alergia):
    
    recomendados=[] #lista de mascotas

    qAlergy= 'MATCH (u:Animal)-[r:Puede_estar_con_alguien_que]->(m:CaracteristicaAlergia) WHERE m.Valor=\"'+alergia+'\" RETURN u'
    porAlergia=driver.query(qAlergy,returns=(client.Node))
    for i in porAlergia:
        recomendados.append(i[0]["Nombre"])

    qActivo='MATCH (u:Animal)-[r:Es_una_mascota]->(m:CaracteristicaTipoM) WHERE m.Valor=\"'+tipo+'\" RETURN u'
    porActivo=driver.query(qActivo,returns=(client.Node))
    for j in porActivo:
        recomendados.append(j[0]["Nombre"])
    
    qTime = 'MATCH (u:Animal)-[r:Cantidad_de_tiempo_que_necesitan]->(m:CaracteristicaTiempo) WHERE m.Valor=\"'+tiempo+'\" RETURN u'
    porTiempo=driver.query(qTime, returns=(client.Node))
    for h in porTiempo:
        recomendados.append(h[0]["Nombre"])
                            

    qSpace='MATCH (u:Animal)-[r:Cantidad_de_espacio_que_necesitan]->(m:CaracteristicaEspacio) WHERE m.Valor=\"'+space+'\" RETURN u'
    porEspacio=driver.query(qSpace,returns=(client.Node))
    for k in porEspacio:
        recomendados.append(k[0]["Nombre"])
    

    qPersonality='MATCH (u:Animal)-[r:Recomendable_para_una_persona]->(m:CaracteristicaPersonalidad) WHERE m.Valor=\"'+personalidad+'\" RETURN u'
    porPersonalidad=driver.query(qPersonality,returns=(client.Node))
    for x in porPersonalidad:
        recomendados.append(x[0]["Nombre"])
    
    qMoney='MATCH (u:Animal)-[r:Costo_mensual_de_manutencion]->(m:CaracteristicaPresupuesto) WHERE m.Valor=\"'+presupuesto+'\" RETURN u'
    porDinero=driver.query(qMoney,returns=(client.Node))
    for l in porDinero:
        recomendados.append(l[0]["Nombre"])

    qKids='MATCH (u:Animal)-[r:Pueden_estar_en_un_hogar_que]->(m:CaracteristicaNinos) WHERE m.Valor=\"'+ninos+'\" RETURN u'
    porNinos=driver.query(qKids,returns=(client.Node))
    for m in porNinos:
        recomendados.append(m[0]["Nombre"])

    qPrevious='MATCH (u:Usuario)-[r:Ha_Tenido]->(s:Animal) WHERE u.Nombre=\"'+nombre+'\" RETURN s'
    yaHaTenido=driver.query(qPrevious,returns=(client.Node))
    for n in porTiempo:
        recomendados.append(n[0]["Nombre"])

    counter=collections.Counter(recomendados)
   
    print counter.most_common(3)
    


