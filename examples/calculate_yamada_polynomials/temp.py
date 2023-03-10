import numpy as np
from yamada.projection import SpatialGraph
from yamada.calculation import Vertex, Edge, Crossing, SpatialGraphDiagram, h_poly, reverse_poly, normalize_yamada_polynomial
import networkx as nx
from cypari import pari

# TODO Create GitHub workflow to run notebook conversion script before each commit (?)

np.random.seed(0)

# Quadrivalent Example
# TODO Debug code for quadrivalent example

# nodes = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
# node_positions = np.array([[0, 0, 0], [1, 0, 0], [0.5, 1, 0], [0.5, 0.5, 0], [0.25,0.75,0], [0.75,0.75,0], [0,1,0], [1,1,0]])
# edges = [('a', 'b'), ('a', 'g'), ('a', 'd'), ('b', 'd'), ('b', 'h'), ('d', 'e'), ('d', 'f'), ('e', 'c'), ('f', 'c'), ('g', 'c'), ('h', 'c')]
#
# sg1 = SpatialGraph(nodes=nodes,
#                    node_positions=node_positions,
#                    edges=edges)
# sg1.project()
# sg1.plot()
# sgd1 = sg1.create_spatial_graph_diagram()
# print("Yamada Polynomial:", sgd1.yamada_polynomial())


# Double-Crossing Single Edge Example
# TODO Check more than one cross per edge (i.e., 2 and 3) works
#
# nodes = ['a', 'b', 'c', 'd', 'e']
# node_positions = np.array([[0,0,0], [1,0,1], [-1,0,1], [-2,0,2], [0,1,3]])
# edges = [('a', 'b'), ('a', 'c'), ('a', 'e'), ('c', 'd'), ('c', 'b'), ('d', 'b'), ('e','b')]
#
# sg1 = SpatialGraph(nodes=nodes,
#                    node_positions=node_positions,
#                    edges=edges)
#
# sg1.project()
# sg1.plot()
#
# sgd1 = sg1.create_spatial_graph_diagram()
#
# print("Yamada Polynomial:", sgd1.normalized_yamada_polynomial())


a = pari('A')

va = Vertex(3, 'a')
vb = Vertex(3, 'b')
vc = Vertex(4, 'c')
vd = Vertex(4, 'd')

va[2] = vc[0]
va[1] = vd[1]
va[0] = vb[2]

vb[0] = vc[3]
vb[1] = vd[2]

vc[1] = vd[0]
vc[2] = vd[3]

D = SpatialGraphDiagram([va, vb, vc, vd])

expected_normalized_yamada_polynomial = normalize_yamada_polynomial(
    -1 * a ** 4 - 3 * a ** 3 - 7 * a ** 2 - 8 * a - 10 - 8 * a ** (-1) - 7 * a ** (-2) - 3 * a ** (-3) - a ** (-4))

assert D.normalized_yamada_polynomial() == expected_normalized_yamada_polynomial