# -*- coding: cp1252 -*-
# Posible ejemplificacion de algortimo de recomendacion
# Maria Fernanda Lopez, Ana Lucia Hernandez, Andrea Arguello
# proyecto #2 - Estructura de datos
#5/05/2018


from neo4jrestclient.client import GraphDatabase
from neo4jrestclient import client
import openpyxl
import sys


driver = GraphDatabase("http://localhost:7474", username="neo4j", password="mypassword")

rangoPresuV = ["1", "2", "3"]
rangoPresu = ["Poco presupuesto", "Regular presupuesto", "Alto presupuesto"]
rangoEspacioV = ["1", "2", "3"]
rangoEspacio = ["Pequeno", "Grande", "Moderado"]
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
espacio = driver.labels.create("CaracteristicaEspacio")
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

#agregar los nodos de personalidad (extrovertido o introvertido) para la personalidad de usuario
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

def add_animal():
    archivo = open("animales.txt", "r")  #esto es supositorio (el nombre)
    contenido = archivo.readlines()
    archivo.close()
    for lineas in contenido:
        animales = lineas.split(", ")
        an = driver.nodes.create(Nombre=animales[0], Presupuesto=animales[1], Alergia=animales[2], Espacio=animales[3], Ninos=animales[4], Tiempo=animales[5], Personalidad=animales[6], Tipo=animales[7])
        animal.add(an)
        esMascota(animales[0], animales[7])
        relacionAA(animales[0], animales[2])
        presupuestoAni(animales[0], animales[1])
        espacioAni(animales[0], animales[3])
        amigable(animales[0], animales[4])
        tiempoAni(animales[0], animales[5])
        personalidadAni(animales[0], animales[6])

    

#-------------------------------------------------------------------------------------------
#----- CREACION DE NODOS EN TIEMPO DE EJECUCION ---------------------
    
def add_usuario(nombre, tenido, espacio, ninos, tiempo, personalidad, tipo, presupuesto, alergia):
    u1 = driver.nodes.create(Nombre=nombre)
    usuarios.add(u1)
    archivo = open("users.txt", "a")
    archivo.write(nombre + ", " + tenido + ", " + str(espacio) + ", " + str(ninos) + ", " + str(tiempo) + ", " + str(personalidad) + ", " + str(tipo) + ", " + str(presupuesto) + ", " + str(alergia)+ "\n")
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
        a.relationships.create("Genera_alergia", al)

def presupuestoAni(animal, presupuesto):
    q = 'MATCH (u:Animal), (s:CaracteristicaPresupuesto) WHERE u.Nombre=\"'+ animal +'\" AND s.Valor=\"'+ presupuesto +'\" RETURN u,s'
    resultados = driver.query(q, returns=(client.Node, client.Node))
    for i in resultados:
        u = i[0]
        pre = i[1]
        a.relationships.create("Presupuesto_animal", pre)

def espacioAni(animal, espacio):
    q = 'MATCH (u:Animal), (s:CaracteristicaEspacio) WHERE u.Nombre=\"'+ animal +'\" AND s.Valor=\"'+ espacio +'\" RETURN u,s'
    resultados = driver.query(q, returns=(client.Node, client.Node))
    for i in resultados:
        u = i[0]
        e = i[1]
        u.relationships.create("Necesita_espacio", e)

def amigable(animal, ninos):
    q = 'MATCH (u:Animal), (s:CaracteristicaNinos) WHERE u.Nombre=\"'+ animal +'\" AND s.Valor=\"'+ ninos +'\" RETURN u,s'
    resultados = driver.query(q, returns=(client.Node, client.Node))
    for i in resultados:
        u = i[0]
        ni = i[1]
        u.relationships.create("Amigable_ninos", ni)

def tiempoAni(animal, tiempo):
    q = 'MATCH (u:Animal), (s:CaracteristicaTiempo) WHERE u.Nombre=\"'+ animal +'\" AND s.Valor=\"'+ tiempo +'\" RETURN u,s'
    resultados = driver.query(q, returns=(client.Node, client.Node))
    for i in resultados:
        u = i[0]
        pre = i[1]
        u.relationships.create("Tiempo_animal", pre)

def personalidadAni(animal, personalidad):
    q = 'MATCH (u:Animal), (s:CaracteristicaPersonalidad) WHERE u.Nombre=\"'+ animal +'\" AND s.Valor=\"'+ personalidad +'\" RETURN u,s'
    resultados = driver.query(q, returns=(client.Node, client.Node))
    for i in resultados:
        u = i[0]
        t = i[1]
        u.relationships.create("Personalidad_animal", t)
    

    
#----------------------------------------------------------------------------------------------------


#------ RELACIONES USUARIOS -----
def haTenido(usuario, animal):
    q = 'MATCH (u:Usuario), (s:CaracteristicaAnimal) WHERE u.Nombre=\"'+ usuario +'\" AND s.Valor=\"'+ animal +'\" RETURN u,s'
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
        a.relationships.create("Presupuesto_usuario", pre)


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
    q = 'MATCH (u:Usuario), (s:Ninos) WHERE u.Nombre=\"'+ usuario +'\" AND s.Valor=\"'+ ninos +'\" RETURN u,s'
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
    d1.relationships.create("CONOCE", p1)

def tiempoUser(usuario, tiempo):
    q = 'MATCH (u:Usuario), (s:Tiempo) WHERE u.Nombre=\"'+ usuario +'\" AND s.Tiempo=\"'+ tiempo +'\" RETURN u,s'
    resultados = driver.query(q, returns=(client.Node, client.Node))
    for i in resultados:
        u = i[0]
        pre = i[1]
        a.relationships.create("Tiempo", pre)


#parcialmente terminado
def registrarInfo(usuario, ninos, tiempo, espacio, tipo, personalidad, alergia, presupuesto):
    relacionNinos(usuarion, ninos)
    relacionUA(usuario, alergia)


#-------------------------------------------------------------------------------------------------------------


# ------- QUERYS -----
def getConocidosUser(nombreUser):
    conocidosL=[]
    q = 'MATCH (u:Usuario)-[r:CONOCE]->(m:Paciente) WHERE u.Nombre=\"'+ nombreUser +'\" RETURN u, type(r), m'
    conocidos = driver.query(q, returns=(client.Node, str, client.Node))
    if len(conocidos) ==0:
        print("\n-----> La persona que ingreso no tiene conocidos o no existe :(")
    else:
        for r in conocidos:
            conocidosL.append(r[2]["Nombre"])
        return conocidosL


add_ninos()
add_personalidad()
add_alergia()
add_tiempo()
add_tipoM()
add_presu()
add_preusuarios()
add_animal()
