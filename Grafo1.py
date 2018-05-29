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

animales = ["Gato", "Perro Grande", "Loro", "Perico", "Canarios", "Perro mediano", "Perro pequeño", "Pez", "Tortuga", "Cotorras", "Agapornis", "Tarantula", "Serpiente", "Hamster", "Lagartos", "Mini piggies", "Ratones", "Cuyos", "Conejos", "Pollos", "Lagartijas", "Urones"]
rangoPresu = ["Poco presupuesto", "Mediano presupuesto", "Alto presupuesto"]
rangoEspacio = ["Pequeno", "Grande", "Moderado"]
ninosPeques = ["Si", "No"]
hrSemana = ["0-3", "4-7", "8-11"]
personalidad = ["Extrovertida", "Introvertida"]


usuario = driver.labels.create("Usuario")
animal = driver.labels.create("Animal")
tiempo = driver.labels.create("Tiempo")
espacio = driver.labels.create("Espacio")
presupuesto = driver.labels.create("Presupuesto")
personalidad = driver.labels.create("Personalidad")
tipoMas = driver.labels.create("TipoM")
ninos = driver.labels.create("Ninos")
personalidad = driver.labels.create("Personalidad")
alergia = driver.labels.create("Alergia")

#-------- CREACION NODOS ---------


def add_preusuarios():
    
def add_usuario(nombre, telefono, correo, edad):
    u1 = driver.nodes.create(Nombre=nombre, Telefono=telefono, Correo=corre, Edad=edad)
    usuarios.add(u1)
    return u1

def add_animal():
    for i in animales:
        an = driver.nodes.create(Nombre=i)
        animal.add(an)

def add_presu():
    for i in rangoPresu:
        pres = driver.nodes.create(Rango=i)
        presupuesto.add(pres)

def add_ninos():
    for i in ninosPeques:
        nn = driver.nodes.crate(Tiene=i)
        ninos.add(nn)

def add_tiempo():
    for i in hrSemana:
        tt = driver.nodes.create(Tiempo=i)
        tiempo.add(tt)

def add_personalidad():
    for i in personalidad:
        pp = driver.nodes.create(Personality=i)    #seria bueno tal vez ponerle otro nombre pero la mera verdad no se me ocurre
        personalidad.add(pp)

def add_alergia():
    for i in ninosPeques:
        al = driver.nodes.create(Posee=i)
        alergia.add(al)


#------ RELACIONES -----

#no cree los nodos de "TipoM" porque como esos estan por default pensaba que los metieramos de una en neo4j de una con los atributos con este nombre
def esMascota(animal, tipo):
    q = 'MATCH (u:Animal), (s:TipoM) WHERE u.Nombre=\"'+ animal +'\" AND s.Tipo=\"'+ tipo +'\" RETURN u,s'
    resultados = driver.query(q, returns=(client.Node, client.Node))
    for i in resultados:
        a = i[0]
        t = i[1]
        a.relationships.create("Es_una_mascota", t)

def haTenido(usuario, animal):
    q = 'MATCH (u:Usuario), (s:Animal) WHERE u.Nombre=\"'+ usuario +'\" AND s.Nombre=\"'+ animal +'\" RETURN u,s'
    resultados = driver.query(q, returns=(client.Node, client.Node))
    for i in resultados:
        u = i[0]
        a = i[1]
        u.relationships.create("Ha_Tenido", a)
        
#no cree los nodos de "Espacio" porque como esos estan por default pensaba que los metieramos de una en neo4j de una con los atributos con este nombre
def espacio(usuario, espacio):
    q = 'MATCH (u:Usuario), (s:Espacio) WHERE u.Nombre=\"'+ usuario +'\" AND s.Tamano=\"'+ espacio +'\" RETURN u,s'
    resultados = driver.query(q, returns=(client.Node, client.Node))
    for i in resultados:
        u = i[0]
        e = i[1]
        u.relationships.create("Espacio_disponible", e)

#no cree los nodos de "TipoM" porque como esos estan por default pensaba que los metieramos de una en neo4j de una con los atributos con este nombre
def prefMas(usuario, tipo):
    q = 'MATCH (u:Usuario), (s:TipoM) WHERE u.Nombre=\"'+ usuario +'\" AND s.Tipo=\"'+ tipo +'\" RETURN u,s'
    resultados = driver.query(q, returns=(client.Node, client.Node))
    for i in resultados:
        u = i[0]
        t = i[1]
        u.relationships.create("Prefiere_una_mascota", t)

#no cree los nodos de "Presupuesto" porque como esos estan por default pensaba que los metieramos de una en neo4j de una con los atributos con este nombre
def relacionPresupuesto(usuario, presupuesto):
    q = 'MATCH (u:Animal), (s:Presupuesto) WHERE u.Nombre=\"'+ usuario +'\" AND s.Rango=\"'+ presupuesto +'\" RETURN u,s'
    resultados = driver.query(q, returns=(client.Node, client.Node))
    for i in resultados:
        u = i[0]
        pre = i[1]
        a.relationships.create("Genera_alergia", pre)

#no cree los nodos de "Alergia" porque como esos estan por default pensaba que los metieramos de una en neo4j de una con los atributos con este nombre
def relacionAA(animal, alergia):
    q = 'MATCH (u:Animal), (s:Alergia) WHERE u.Nombre=\"'+ animal +'\" AND s.Posee=\"'+ alergia +'\" RETURN u,s'
    resultados = driver.query(q, returns=(client.Node, client.Node))
    for i in resultados:
        a = i[0]
        al = i[1]
        a.relationships.create("Genera_alergia", al)


#no cree los nodos de "Alergia" porque como esos estan por default pensaba que los metieramos de una en neo4j de una con los atributos con este nombre
def relacionUA(usuario, alergia):
    q = 'MATCH (u:Usuario), (s:Alergia) WHERE u.Nombre=\"'+ usuario +'\" AND s.Posee=\"'+ alergia +'\" RETURN u,s'
    resultados = driver.query(q, returns=(client.Node, client.Node))
    for i in resultados:
        u = i[0]
        al = i[1]
        u.relationships.create("Tiene_alergia", al)

#no cree los nodos de "Ninos" porque como esos estan por default pensaba que los metieramos de una en neo4j de una con los atributos con este nombre
def relacionNinos(usuario, ninos):
    q = 'MATCH (u:Usuario), (s:Ninos) WHERE u.Nombre=\"'+ usuario +'\" AND s.Tiene=\"'+ ninos +'\" RETURN u,s'
    resultados = driver.query(q, returns=(client.Node, client.Node))
    for i in resultados:
        u = i[0]
        ni = i[1]
        u.relationships.create("Tiene_ninos", ni)
    

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

def registrarInfo(usuario, ninos, tiempo, espacio, tipo, personalidad, alergia, presupuesto):
    relacionNinos(usuarion, ninos)
    relacionUA(usuario, alergia)
    


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
    


            



