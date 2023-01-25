import networkx as nx


class Graph:
    """
    Class to contain a graph and your bfs function
    
    You may add any functions you deem necessary to the class
    """

    def __init__(self, filename: str):
        """
        Initialization of graph object 
        """
        self.graph = nx.read_adjlist(filename, create_using=nx.DiGraph, delimiter=";")

    def bfs(self, start, end=None):
        """
        TODO: write a method that performs a breadth first traversal and pathfinding on graph G

        * If there's no end node input, return a list nodes with the order of BFS traversal
        * If there is an end node input and a path exists, return a list of nodes with the order of the shortest path
        * If there is an end node input and a path does not exist, return None

        """
        # First get the graph g
        g = self.graph

        # Initialize empty lists that contain visited nodes and the queue
        visited = []
        queue = []

        # Now check if graph is empty and if start and end node exist
        # Raise exceptions if an invalid graph, start or end node is provided

        if len(g.edges) > 0:
            if start in g.nodes():
                print("Starting at:", start)
                # Initialize the queue list with the start node
                queue.append([start])
                if end is not None and end not in g.nodes():
                    raise ValueError("End node not found in graph")
                elif end is not None:
                    print("Looking for:", end)
                else:
                    print("Traversing graph from start node")
            elif end not in g.nodes:
                raise ValueError("Start and End node not found in graph")
            else:
                raise ValueError("Start node not found in graph")
        else:
            raise ValueError("Graph is empty")

        # Check to make sure starting node has neighbors
        if len(g[start]) == 0:
            raise ValueError("Start node has no neighbors")

        # BFS Traversal
        # Start moving through the queue
        while queue:
            # Get the next path in the queue
            path_survey = queue.pop(0)
            # Get the last node in the path being surveyed
            node_survey = path_survey[-1]
            # Now if the last node in the path hasn't been visited yet, we will go through the neighbors of the node and
            # We will add the neighbor to the path (this is how we keep track of the paths that have been surveyed)
            # Then add the new path to the queue
            # Add the node that is being surveyed to the visited list
            if node_survey not in visited:
                for neighbor in g[node_survey]:
                    path_new = list(path_survey)
                    path_new.append(neighbor)
                    queue.append(path_new)

                    if neighbor == end:
                        return path_new
                visited.append(node_survey)

        # Return the entire visited list if there is no path
        if end is None:
            return visited

        # Check to see if end has not been reached and return None
        if end is not None and end not in visited:
            return None
