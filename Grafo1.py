# Posible ejemplificacion de algortimo de recomendacion
# Maria Fernanda Lopez, Ana Lucia Hernandez, Andrea Arguello
# proyecto #2 - Estructura de datos
#5/05/2018


from neo4jrestclient.client import GraphDatabase
from neo4jrestclient import client
import sys


driver = GraphDatabase("http://localhost:7474", username="neo4j", password="mypassword")



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
#Yo diria que los unicos nodos que tenemos que hacer son los de los usuarios porque los otros ya los tendriamos en la base de datos metidos por default
#porque no e como que fueramos a pedir info de animales o si?
def add_usuario(nombre, telefono, correo, edad):
    u1 = driver.nodes.create(Nombre=nombre, Telefono=telefono, Correo=corre, Edad=edad)
    usuarios.add(u1)
    return u1


#------ RELACIONES -----
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

def espacio(usuario, espacio):
    q = 'MATCH (u:Usuario), (s:Espacio) WHERE u.Nombre=\"'+ usuario +'\" AND s.Tamano=\"'+ espacio +'\" RETURN u,s'
    resultados = driver.query(q, returns=(client.Node, client.Node))
    for i in resultados:
        u = i[0]
        e = i[1]
        u.relationships.create("Espacio_disponible", e)

def prefMas(usuario, tipo):
    q = 'MATCH (u:Usuario), (s:TipoM) WHERE u.Nombre=\"'+ usuario +'\" AND s.Tipo=\"'+ tipo +'\" RETURN u,s'
    resultados = driver.query(q, returns=(client.Node, client.Node))
    for i in resultados:
        u = i[0]
        t = i[1]
        u.relationships.create("Prefiere_una_mascota", t)

def relacionAA(animal, alergia):
    q = 'MATCH (u:Animal), (s:Alergia) WHERE u.Nombre=\"'+ animal +'\" AND s.Posee=\"'+ alergia +'\" RETURN u,s'
    resultados = driver.query(q, returns=(client.Node, client.Node))
    for i in resultados:
        a = i[0]
        al = i[1]
        a.relationships.create("Genera_alergia", al)

def relacionUA(usuario, alergia):
    q = 'MATCH (u:Usuario), (s:Alergia) WHERE u.Nombre=\"'+ usuario +'\" AND s.Posee=\"'+ alergia +'\" RETURN u,s'
    resultados = driver.query(q, returns=(client.Node, client.Node))
    for i in resultados:
        u = i[0]
        al = i[1]
        u.relationships.create("Tiene_alergia", al)
        


            



