# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 16:12:20 2015

@author: hina
"""
# code adapted from here:
# https://github.com/maksim2042/SNABook

# We often want to be able to traverse the structure of a graph or network
#     to find the shortest path from node A to node B, or to understand the 
#     structure of the graph. 

# Terminology:
#     A leaf node is a node with only one incoming connection.
#     A child node is a node connected to a starting node; 
#         the starting node then is a parent node.
#     Two child nodes of a single parent node are sibling nodes.

print()

import matplotlib.pyplot
import networkx
from networkx import algorithms
from networkx import generators

G = generators.small.bull_graph()
#G = networkx.generators.diamond_graph()
#G = networkx.generators.small.krackhardt_kite_graph()
#G = networkx.karate_club_graph()

# Depth First Search:
#     Go deep before going broad.
#     visit the neighbor's neighbors first and
#     only then proceed to the neighbors
print ("Depth First Search")
print (list(algorithms.traversal.dfs_edges(G, 0)))
print ()

# Breadth First Search:
#     visit all of the immediate neighbors first and 
#     only then proceeds to their neighbors.
print ("Breadth First Search")
print (list(algorithms.traversal.bfs_edges(G, 0)))
print ()

# A walk is an alternating sequence of nodes and edges that connect them.
#    A walk is simple if no node is crossed twice.
#    A walk is open if the starting and ending nodes are different.
#    A walk is closed if the starting and ending nodes are the same.
#    The length of the walk is the number of edges.
#    A path is an open simple walk. A path can have lenght 0.
#    A cycle is a closed simple walk. A cycle can not have lenght 0.
print ("Shortest Path")
print (algorithms.shortest_path(G,0,3))
print ()

print ("Average Shortest Path")
print (algorithms.all_pairs_shortest_path(G))
print (algorithms.average_shortest_path_length(G))
print ()

# Graph Distance:
#    Unweighted distance - number of edges between two nodes
#    Weighted distance - sum of weights between two nodes. 
#        so shortest path is least combined weight, not necessarily the fewest nodes
#    Euclidean distance -  between the two nodes in the adjacency matrix: which is
#        proportional to the number of common neighbors shared between the nodes.
#

# Dijkstra's Algorithm:
#    for a given vertex it finds the lowest cost path to all other vertices, 
#    where “cost” is determined by summing edge weights. In graphs where edge 
#    weights correspond to distance (in unweighted graphs the weights are 
#    assumed to be one) the found path is the shortest. 
#    The algorithm can also determine the lowest cost path between two given 
#    vertices.
print (algorithms.dijkstra_path(G, 0, 3))
print (algorithms.dijkstra_predecessor_and_distance(G, 0, 3))

pos=networkx.spring_layout(G)
networkx.draw_networkx_nodes(G,pos)
networkx.draw_networkx_edges(G,pos)
networkx.draw_networkx_labels(G,pos)
matplotlib.pyplot.axis('off')
matplotlib.pyplot.savefig("graphTraversals.png") 
matplotlib.pyplot.show() 