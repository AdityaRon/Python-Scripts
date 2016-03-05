# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 14:03:50 2015

@author: hina
"""

# code adapted from here:
# https://github.com/maksim2042/SNABook

# Social Networks are graphs.
# A graph is a collection of Nodes and Edges.
# Edges can be Directed, and can have Weight.

print()

import matplotlib.pyplot
import networkx
import networkx.generators.small

#G = networkx.generators.small.bull_graph()
# G = networkx.generators.diamond_graph()
G = networkx.generators.small.krackhardt_kite_graph()
# G = networkx.karate_club_graph()

print ("Number of Nodes:")
print (G.number_of_nodes()) # same as len(G)
print ()

print ("Number of Edges:")
print (G.number_of_edges())
print ()

# density is (number of potential edges) / (number of actual edges)
# for an undirected graph with n nodes and m edges
#     number potential edges = n(n-1)/2
#     number actual edges = m
#     density = 2m/[n*(n-1)]
# for an undirected graph with n nodes
#     number potential edges = n(n-1)
#     number actual edges = m
#     density = m/[n*(n-1)]
print ("Density:")
print (networkx.density(G))
print ()

# diameter is the longest distance between any two nodes in the graph
print ("Diameter:")
print (networkx.diameter(G))
print ()

# Adjacency Matrix - ex: a 1 in cell A-B means there’s an edge between them
#      A B C D E
#    A 0 1 0 1 1
#    B 1 0 0 1 0
#    C 0 0 0 1 1
#    D 1 1 1 0 0
#    E 1 0 1 0 0
print ("Adjacency Matrix:")
adjacencyList = G.adjacency_list()
for n in networkx.nodes(G):
    print(n, adjacencyList[n])

pos=networkx.spring_layout(G)
networkx.draw_networkx_nodes(G,pos)
networkx.draw_networkx_edges(G,pos)
networkx.draw_networkx_labels(G,pos)
matplotlib.pyplot.axis('off')
matplotlib.pyplot.savefig("nodeMeasures.png") 
matplotlib.pyplot.show() 


