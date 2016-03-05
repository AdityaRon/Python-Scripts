# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 17:04:04 2015

@author: hina
"""

# twitter data and code adapted from here:
# https://github.com/maksim2042/SNABook

print ()

import matplotlib.pyplot
import networkx
import networkx.generators.small
from networkx import generators

# G = networkx.generators.small.bull_graph()
# G = networkx.generators.diamond_graph()
# G = networkx.generators.small.krackhardt_kite_graph()
# G = networkx.karate_club_graph()

# twitter retweet network:
#     twitter users are nodes; retweets are links between nodes
#     over time people tend to retweet from those they trust
#     so over time a twitter retweet network is a proxy for trust networks
G=networkx.read_pajek("C:/Users/Aditya/Desktop/CIS 509/Week 7/SocialNetworkAnalysis/data/egypt_retweets.net")

print ("Number of Nodes:")
print (G.number_of_nodes())
print ()

print ("Number of Edges:")
print (G.number_of_edges())
print ()

# Subgraph: 
#     subset of nodes in a network, along with all of the edges linking these nodes. 
#
# Component Subgraph (or simply Component): 
#     portions of the network that are disconnected from each other. 

print ("Number of Component Subgraphs:")
print (len(list(networkx.connected_component_subgraphs(G))))
print ()

print ("Number of Nodes in Component Subgraphs with > 10 Nodes:")
x=[len(c) for c in networkx.connected_component_subgraphs(G) if len(c) > 10]
print (x)
print ()

# Islands:
#     trim edges that are weak (ex: only retain edges with >= 25 retweets).
#     what remains is subcores of maximal activity between nodes that have 
#         developed a trust relationship.

def trim_edges(g, threshold=1):
    gtmp = networkx.Graph()
    for f, to, edata in g.edges(data=True):
        if edata['weight'] > threshold:
            gtmp.add_edge(f,to,edata)
    return gtmp

print ('Threshold', 'Nodes', 'Islands')
for threshold in range(0,25):
    g = trim_edges(G, threshold)
    print (threshold, g.number_of_nodes(), len(list(networkx.connected_component_subgraphs(g))))
print ()

# Ego Networks:
#     subnetworks that are centered on a certain node.
#     derived by running a breath-first search, and limiting depth to <= 3.
#         intuitivel this is becuase, we know our friends quite well, 
#         our friends’ friends somewhat well, 
#         and our friends’ friends’ friends almost not at all.

ben = networkx.Graph(networkx.ego_graph(G, 'justinbieber', radius=3))
gen = networkx.Graph(networkx.ego_graph(G, 'Ghonim', radius=3))
print ('Ego(r=3)', 'Nodes', 'Edges')
print ('Beiber', ben.number_of_nodes(), ben.number_of_edges())
print ('Ghonim', gen.number_of_nodes(), gen.number_of_edges())
print ()

# Clustering Coefficient:
#     measures the proportion of teh ego's friends that are also friends with each other  
#     star networks with a single broadcast node and passive listeners have a low clustering coefficient.
#     dense ego networks with a lot of mutual trust have a high clustering coefficient.

ben = networkx.Graph(networkx.ego_graph(G, 'justinbieber', radius=1))
gen = networkx.Graph(networkx.ego_graph(G, 'Ghonim', radius=1))
print ('Ego(r=1)', 'Nodes', 'Edges', 'ClusCoeff')
print ('Beiber', ben.number_of_nodes(), ben.number_of_edges(), networkx.average_clustering(ben))
print ('Ghonim', gen.number_of_nodes(), gen.number_of_edges(), networkx.average_clustering(gen))
print ()

# Cliques:
#     A clique is defined as a maximal complete subgraph of a given graph—i.e., 
#     a group of people where everybody is connected directly to everyone else. 
# we could find cliques for the twitter data above but since that can take time,
# we will look at the bull_graph instead
G = generators.small.bull_graph()
print (list(networkx.find_cliques(G)))