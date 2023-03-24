#!/usr/bin/env python
# coding: utf-8

# 

# In[1]:


import numpy as np
from yamada import SpatialGraph
from yamada import Vertex, Edge, Crossing, SpatialGraphDiagram, h_poly, reverse_poly, normalize_yamada_polynomial

np.random.seed(0)


# ## Verifying the cyclic ordering of nodes for a vertex
# 
# ![Abstract Graph G5](./images/abstract_graph_G5.png)

# In[2]:


def test_cyclic_node_ordering_vertex():

    nodes = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

    node_positions = np.array([[0, 0, 0], [1, 0, 0], [0.5, 1, 0], [0.5, 0.5, 0], [0.25,0.75, 0], [0.75, 0.75, 0], [0, 1, 0], [1, 1, 0]])

    edges = [('a', 'b'), ('a', 'g'), ('a', 'd'), ('b', 'd'), ('b', 'h'), ('d', 'e'), ('d', 'f'), ('e', 'c'), ('f', 'c'), ('g', 'c'), ('h', 'c')]

    sg = SpatialGraph(nodes=nodes,
                      node_positions=node_positions,
                      edges=edges)

    sg.project()

    order = sg.cyclic_node_ordering_vertex('c')
    expected_order = {'c': {'e': 3, 'f': 0, 'g': 2, 'h': 1}}

    assert order == expected_order


# ## Verify the cyclic ordering of nodes for a crossing
# 
# ![Crossing Ordering](./images/crossing_ordering.png)

# In[3]:


def test_cyclic_ordering_crossing():

    np.random.seed(0)

    component_a = 'c_a'
    component_b = 'c_b'
    component_c = 'c_c'
    component_d = 'c_d'
    component_e = 'c_e'
    component_f = 'c_f'
    component_g = 'c_g'
    component_h = 'c_h'

    waypoint_ab = 'w_ab'
    waypoint_ad = 'w_ad'
    waypoint_ae = 'w_ae'
    waypoint_bc = 'w_bc'
    waypoint_bf = 'w_bf'
    waypoint_cd = 'w_cd'
    waypoint_cg = 'w_cg'
    waypoint_dh = 'w_dh'
    waypoint_ef = 'w_ef'
    waypoint_eh = 'w_eh'
    waypoint_fg = 'w_fg'
    waypoint_gh = 'w_gh'

    nodes = [component_a, component_b, component_c, component_d, component_e, component_f,
             component_g, component_h, waypoint_ab, waypoint_ad, waypoint_ae, waypoint_bc,
             waypoint_bf, waypoint_cd, waypoint_cg, waypoint_dh, waypoint_ef, waypoint_eh,
             waypoint_fg, waypoint_gh]

    component_positions = np.array([[0, 0, 0],  # a
                                [1, 0, 0],  # b
                                [1, 1, 0],  # c
                                [0, 1, 0],  # d
                                [0, 0, 1],  # e
                                [1, 0, 1],  # f
                                [1, 1, 1],  # g
                                [0, 1, 1]])  # h

    waypoint_positions = np.array([[0.5, 0, 0],  # ab
                               [0, 0.5, 0],  # ad
                               [0, 0, 0.5],  # ae
                               [1, 0.5, 0],  # bc
                               [1, 0, 0.5],  # bf
                               [0.5, 1, 0],  # cd
                               [1, 1, 0.5],  # cg
                               [0, 1, 0.5],  # dh
                               [0.5, 0, 1],  # ef
                               [0, 0.5, 1],  # eh
                               [1, 0.5, 1],  # fg
                               [0.5, 1, 1]])  # gh

    node_positions = np.concatenate((component_positions, waypoint_positions), axis=0)

    edges = [(component_a, waypoint_ab), (waypoint_ab, component_b),
         (component_a, waypoint_ad), (waypoint_ad, component_d),
         (component_a, waypoint_ae), (waypoint_ae, component_e),
         (component_b, waypoint_bc), (waypoint_bc, component_c),
         (component_b, waypoint_bf), (waypoint_bf, component_f),
         (component_c, waypoint_cd), (waypoint_cd, component_d),
         (component_c, waypoint_cg), (waypoint_cg, component_g),
         (component_d, waypoint_dh), (waypoint_dh, component_h),
         (component_e, waypoint_ef), (waypoint_ef, component_f),
         (component_e, waypoint_eh), (waypoint_eh, component_h),
         (component_f, waypoint_fg), (waypoint_fg, component_g),
         (component_g, waypoint_gh), (waypoint_gh, component_h)]


    sg = SpatialGraph(nodes=nodes, node_positions=list(node_positions), edges=edges)

    ordering_dict = sg.cyclic_node_ordering_crossings()

    expected_dict = {'crossing_0': {'c_f': 0, 'c_c': 1, 'w_ef': 2, 'w_bc': 3},
                     'crossing_1': {'w_eh': 0, 'c_d': 1, 'c_e': 2, 'w_cd': 3}}

    assert ordering_dict == expected_dict


# ## Divide edges into sub-edges
# 
# ![Infinity Symbol](./images/infinity_symbol.png)
# 
# 

# In[4]:


def test_get_sub_edges():

    np.random.seed(0)

    sg = SpatialGraph(nodes=['a', 'b', 'c', 'd'],
                      node_positions=np.array([[0, 0.5, 0], [1, 0.5, 1], [1, 0, 0], [0, 0, 1]]),
                      edges=[('a', 'b'), ('b', 'c'), ('c', 'd'), ('d', 'a')])

    sep = sg.get_sub_edges()

    expected_sub_edges = [('b', 'crossing_0'), ('crossing_0', 'a'), ('b', 'c'), ('d', 'crossing_0'), ('crossing_0', 'c'), ('d', 'a')]

    assert sep == expected_sub_edges


# In[4]:



