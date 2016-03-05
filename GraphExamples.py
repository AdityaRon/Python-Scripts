# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 08:37:17 2015

@author: hina
"""

# code adapted from here:
# https://github.com/maksim2042/SNABook

print()

import matplotlib.pyplot
import networkx
import networkx.generators.small

G = networkx.generators.small.bull_graph()
#G = networkx.generators.diamond_graph()
#G = networkx.generators.small.krackhardt_kite_graph()
#G = networkx.karate_club_graph()

pos=networkx.spring_layout(G)
networkx.draw_networkx_nodes(G,pos)
networkx.draw_networkx_edges(G,pos)
networkx.draw_networkx_labels(G,pos)
matplotlib.pyplot.axis('off')
matplotlib.pyplot.savefig("graphExamples.png") 
matplotlib.pyplot.show()