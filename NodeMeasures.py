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
adjacencyList = G.adjacency_list()

# Degree Centrality (celebrities): 
#     number of connections that a node has
degreeCentrality = networkx.degree(G)
#print (degreeCentrality)

# Closeness Centrality (gossipmongers):
#     compute shortest path between every pair of nodes using Dijkstra’s algorithm
#     then for every node:
#         compute average (shortest) distance to all other nodes
#         divide by maximum distance (normalizes to 0-1 range)
#         closeness = 1 divided by average distance 
closenessCentrality = networkx.closeness_centrality(G)
#print (closenessCentrality)

# Betweenness Centrality (bottlenecks or bridges or boundary spanners):
#    compute shortest paths between every pair of nodes using Dijkstra's algorithm
#    then for every node:
#        count the number of shortest paths that node is on
#        divide by maximum numer of shortest paths (normalizes to 0-1 range)
betweennessCentrality = networkx.betweenness_centrality(G)
#print (betweennessCentrality)

# Eigenvector Centrality (grey cardinals - powerful but behind the scenes):
#    recursive version of degree centrality... node high on eigenvector centrality 
#    is essentially connected to many high degree nodes
eigenvectorCentrality = networkx.eigenvector_centrality(G)
#print (eigenvectorCentrality)

printFormat = "{0:<5} {1:<7} {2:<10} {3:<12} {4:<12} {5}"
print(printFormat.format('Node', 'Degree', 'Closeness', 'Betweenness', 'Eigenvector', 'Adjacency'))
for n in networkx.nodes(G):
    print(printFormat.format(n, round(degreeCentrality[n],2), round(closenessCentrality[n],2), round(betweennessCentrality[n],2), round(eigenvectorCentrality[n],2), adjacencyList[n]))

pos=networkx.spring_layout(G)
networkx.draw_networkx_nodes(G,pos)
networkx.draw_networkx_edges(G,pos)
networkx.draw_networkx_labels(G,pos)
matplotlib.pyplot.axis('off')
matplotlib.pyplot.savefig("nodeMeasures.png") 
matplotlib.pyplot.show() 


