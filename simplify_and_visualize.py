# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 15:33:51 2019

@author: le3
"""

import networkx as nx
import numpy as np
import planarity
import progressbar
from scipy.spatial.distance import squareform


def simplify_using_PMFG(corr_matrix): 

    #get the list of decreasing weighted links
    rholist = []
    n = len(corr_matrix)
    for i in range(n): 
        for j in range(n): 
            if i<j:
                if corr_matrix[i][j] != 0:
                    rholist.append([abs(float(corr_matrix[i][j])),i,j])
                
    rholist.sort(key=lambda x: x[0])
    rholist.reverse()
    
    m = len(rholist)
    filtered_matr = np.zeros((n, n))
    control = 0


    with progressbar.ProgressBar(max_value=m) as bar:
    #get the filtered adjacency matrix using PMFG algorithm
        for t in range(m): 
            if control <= 3 * (n - 2) - 1: 
                i = rholist[t][1]
                j = rholist[t][2]
                filtered_matr[i][j] = rholist[t][0]

                #check planarity here
                G = nx.Graph()
                for i in range(0,n): 
                    for j in range(0,n): 
                        if filtered_matr[i][j] != 0:
                            G.add_edge(int(i),int(j),weight = filtered_matr[i][j])
                if planarity.is_planar(G) == False: 
                    filtered_matr[i][j] = 0
                    control = control +1
            bar.update(t)
    
    #build the network
    PMFG = nx.Graph()
    for i in range(0,n): 
        for j in range(0,n): 
            if filtered_matr[i][j] != 0:
                PMFG.add_edge(int(i),int(j),weight = filtered_matr[i][j])
    
    return PMFG
def simplify_using_spanningTree(G):
    T = nx.minimum_spanning_tree(G)
    return T

def sort_graph_edges(G):
    sorted_edges = []
    for source, dest, data in sorted(G.edges(data=True),
                                     key=lambda x: x[2]['weight']):
        sorted_edges.append({'source': source,
                             'dest': dest,
                             'weight': data['weight']})
    return sorted_edges

def compute_PMFG(sorted_edges, nb_nodes):
    PMFG = nx.Graph()
    for edge in sorted_edges:
        PMFG.add_edge(edge['source'], edge['dest'])
        if not planarity.is_planar(PMFG):
            PMFG.remove_edge(edge['source'], edge['dest'])
            
        if len(PMFG.edges()) == 3*(nb_nodes-2):
            break
    
    return PMFG
    

    
def testCase_investor_network():
    fn = 'corr_nokia.gexf'
    G = nx.read_gexf(fn)
    sorted_edges = sort_graph_edges(G)
    G2 = compute_PMFG(sorted_edges, len(G.nodes))  
    return G2
    
def testcase_simulate_graph():
    nb_nodes = 150
    distances = squareform(np.random.uniform(
        size=int(nb_nodes * (nb_nodes - 1) / 2)))
    distances[np.diag_indices(nb_nodes)] = np.ones(nb_nodes)
    complete_graph = nx.Graph()
    for i in range(nb_nodes):
        for j in range(i+1, nb_nodes):
            complete_graph.add_edge(i, j, weight=distances[i,j])
    
    sorted_edges = sort_graph_edges(complete_graph)
    
    result = compute_PMFG(sorted_edges, len(complete_graph.nodes))  
    return result