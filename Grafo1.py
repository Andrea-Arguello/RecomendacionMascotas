# Posible ejemplificacion de algortimo de recomendacion
# Maria Fernanda Lopez, Ana Lucia Hernandez, Andrea Arguello
# proyecto #2 - Estructura de datos
#5/05/2018

import networkx as nx
G = nx.DiGraph()

# agegar nodos
G.add_node("Maria")
G.add_node("Perro mediano")
G.add_node("Erick")
G.add_node("Ana")
G.add_node("Si")
G.add_node("No")
G.add_node("Grande")
G.add_node("Pequeno")
G.add_node("Mediano")
G.add_node("Activo")
G.add_node("No activo")
G.add_node("No tiene ninos")
G.add_node("0-3")
G.add_node("4-7")
G.add_node("8-11")
G.add_node("Alto P.")
G.add_node("Bajo P.")
G.add_node("Introvertido")
G.add_node("Extrovertido")
G.add_node("Tiene ninos")
G.add_node("Regular P.")
G.add_node("Gato")
G.add_node("Hamster")


print ("Nodos: ", G.nodes())

# agregar aristas (relaciones)
G.add_edge("Maria", "Regular P.")
G.add_edge("Maria", "Si")
G.add_edge("Maria", "Mediano")
G.add_edge("Maria", "No tiene ninos")
G.add_edge("Maria", "4-7")
G.add_edge("Maria", "Extrovertido")
G.add_edge("Maria", "No activo")
G.add_edge("Erick", "Alto P.")
G.add_edge("Erick", "No")
G.add_edge("Erick", "Pequeno")
G.add_edge("Erick", "No tiene ninos")
G.add_edge("Erick", "4-7")
G.add_edge("Erick", "Introvertido")
G.add_edge("Erick", "Activo")
G.add_edge("Ana", "Bajo P.")
G.add_edge("Ana", "Si")
G.add_edge("Ana", "Hamster")
G.add_edge("Ana", "Mediano")
G.add_edge("Ana", "8-11")
G.add_edge("Ana", "Tiene ninos")
G.add_edge("Ana", "Extrovertido")
G.add_edge("Ana", "Activo")
G.add_edge("Regular P.", "Perro mediano")
G.add_edge("Si", "Perro mediano")
G.add_edge("Grande", "Perro mediano")
G.add_edge("Tiene ninos", "Perro mediano")
G.add_edge("4-7", "Perro mediano")
G.add_edge("Introvertido", "Perro mediano")
G.add_edge("Activo", "Perro mediano")
G.add_edge("Bajo P.", "Gato")
G.add_edge("Si", "Gato")
G.add_edge("Mediano", "Gato")
G.add_edge("Tiene ninos", "Gato")
G.add_edge("4-7", "Gato")
G.add_edge("Extrovertido", "Gato")
G.add_edge("No activo", "Gato")
G.add_edge("Bajo P.", "Hamster")
G.add_edge("Si", "Hamster")
G.add_edge("Pequeno", "Hamster")
G.add_edge("No tiene ninos", "Hamster")
G.add_edge("8-11", "Hamster")
G.add_edge("Introvertido", "Hamster")
G.add_edge("No activo", "Hamster")

print ("Aristas: ", G.edges())

# Breath First Search

print ("BFS:")
print (list(nx.bfs_tree(G,"Maria")))
#print (nx.bfs_successors(G,"Maria"))


print ("DFS:")
#print (list(nx.dfs_preorder_nodes(G,"Ana")))



