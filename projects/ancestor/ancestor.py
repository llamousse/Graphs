# use graph from day 1 to assist with today's assignment
from graph import Graph

def earliest_ancestor(ancestors, starting_node):
    # create new graph
    g = Graph()

    # add vertex and edges for parent and child in ancestors
    for (parent, child) in ancestors:
        g.add_vertex(parent)
        g.add_vertex(child)

    for (parent, child) in ancestors:
        g.add_edge(parent, child)

    # create new list to store longest path
    longest = []

    # find path to starting node in ancestors
    for (parent, child) in ancestors:
        path = g.dfs(parent, starting_node)
        # if path is longer than starting_node
        # longest will replace old path
        if path is not None and len(path) > len(longest):
            longest = path.copy()

    # return ancestor
    # if doesn't have starting node value then return -1
    return longest[0] if len(longest) > 1 else -1