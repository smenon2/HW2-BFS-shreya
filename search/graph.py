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

        # Initialize the lists that contain visited nodes and the queue
        visited = []
        queue = []

        # Now check if graph is empty, if start and end node exist
        # Initialize the visited and queue list with the start node

        if len(g.edges) > 0:
            if start in g.nodes():
                print("Starting at:", start)
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
        # Break out of the loop if the end is reached and this will
        break_out_flag = False

        while queue:
            path_survey = queue.pop(0)
            node_survey = path_survey[-1]
            if node_survey not in visited:
                for neighbor in g[node_survey]:
                    path_new = list(path_survey)
                    path_new.append(neighbor)
                    queue.append(path_new)

                    if neighbor == end:
                        return path_new
                visited.append(node_survey)

        if end is None:
            return visited

        # Check to see if end has not been reached and return None
        if end is not None and end not in visited:
            return None
