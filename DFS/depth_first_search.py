#!/usr/bin/env python3

"""
This module defines functions for depth-first-search in a graph with a given adjacency list
"""

def dfs_visit(node_list, adj_list, root_node, parent):
    """
    Takes the graph node list, its adj list, and a node s,
    and visits all the nodes reachable from s recursively.
    """
    for node in adj_list[root_node]:
        if node not in parent:
            parent[node] = root_node
            dfs_visit(node_list, adj_list, node, parent)

def dfs(node_list, adj_list):
    """
    Iterate over possible root_nodes to explore the whole graph
    """
    parent = {}
    for root_node in node_list:
        if root_node not in parent:
            parent[root_node] = None
            dfs_visit(node_list, adj_list, root_node, parent)
