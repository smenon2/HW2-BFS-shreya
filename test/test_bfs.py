# write tests for bfs
import pytest
from search import graph
import networkx as nx
import unittest
import pathlib


def test_bfs_traversal():
    """
    TODO: Write your unit test for a breadth-first
    traversal here. Create an instance of your Graph class 
    using the 'tiny_network.adjlist' file and assert 
    that all nodes are being traversed (ie. returns 
    the right number of nodes, in the right order, etc.)
    """
    data_dir = pathlib.Path(__file__).resolve().parent.parent / "data"
    graph_file = data_dir / 'tiny_network.adjlist'
    G = graph.Graph(graph_file)
    # Creating BFS starting with Martin Kampmann
    vis = G.bfs('Martin Kampmann')

    # Creating ground truth for traversal:
    # I'm including this one just as an example of unit test that doesn't rely on the networkx function
    trav_true = ['Martin Kampmann', '33483487', '32790644', '31806696',
                 '31626775', '31540829', 'Luke Gilbert', 'Steven Altschuler',
                 'Lani Wu', 'Neil Risch', 'Nevan Krogan', '32036252',
                 '32042149', '30727954', '29700475', '34272374', '32353859',
                 '30944313', 'Hani Goodarzi', 'Michael McManus', 'Michael Keiser',
                 'Atul Butte', 'Marina Sirota', '33232663', '32025019', '33765435',
                 '33242416', '31395880', '31486345', 'Charles Chiu']

    # Create a ground truth using the bfs from networkx function
    true_bfs_edges = list(nx.bfs_edges(G.graph, source='Martin Kampmann'))
    # Returned edges, convert tuple list to list and then pull unique nodes
    out = [item for t in true_bfs_edges for item in t]
    res_list = []
    for item in out:
        if item not in res_list:
            res_list.append(item)

    assert len(vis) == len(G.graph.nodes()), "BFS Traversal not getting right number of nodes"
    assert vis == trav_true, "Nodes are not in the right order, compared to hard coded truth"
    assert vis == res_list, "Nodes are not in the right order, compared to networkx BFS"


def test_bfs():
    """
    TODO: Write your unit test for your breadth-first 
    search here. You should generate an instance of a Graph
    class using the 'citation_network.adjlist' file 
    and assert that nodes that are connected return 
    a (shortest) path between them.
    
    Include an additional test for nodes that are not connected 
    which should return None. 
    """

    # First we can check to see if my bfs returns the shortest path using simple case
    # We can test it against the networkx functions
    data_dir = pathlib.Path(__file__).resolve().parent.parent / "data"
    graph_file = data_dir / 'citation_network.adjlist'
    G = graph.Graph(graph_file)

    vis1 = G.bfs('Martin Kampmann', 'Ryan Corces')
    network_path = nx.shortest_path(G.graph, source='Martin Kampmann', target='Ryan Corces')

    # Again here is the ground truth from reading the citation_network adjacency list
    # Included to show unit test without relying on networkx functions

    ground_truth = ['Martin Kampmann', '34016988', 'Ryan Corces']

    # Now testing to see if none is returned with disconnected graph:
    vis2 = G.bfs('Martin Kampmann', 'Reza Abbasi-Asl')

    assert vis1 == network_path, "BFS is not returning shortest path (networkx function)"
    assert vis1 == ground_truth, "BFS not returning shortest path (ground truth)"
    assert vis2 is None, "BFS not returning none for disconnected nodes"


def test_edge_empty():
    """
    Here I'm testing a few edges cases - empty graph
    """
    # First I'll test an empty graph
    data_dir = pathlib.Path(__file__).resolve().parent.parent / "test"
    graph_file = data_dir / 'empty.adjlist'
    G = graph.Graph(graph_file)

    try:
        vis = G.bfs('Martin Kampmann')
    except ValueError:
        # The exception was raised as expected
        pass
    else:
        # If we get here, then the ValueError was not raised
        # raise an exception so that the test fails
        raise AssertionError("ValueError was not raised when passed empty graph")


def test_edge_no_start():
    """
    Here I'm testing a few edges cases - start node that doesn't exist
    """
    # Testing with start node that doesn't exist in the graph
    data_dir = pathlib.Path(__file__).resolve().parent.parent / "data"
    graph_file = data_dir / 'citation_network.adjlist'
    G = graph.Graph(graph_file)

    try:
        vis = G.bfs('Martin Kampmann1')
    except ValueError:
        # The exception was raised as expected
        pass
    else:
        # If we get here, then the ValueError was not raised
        # raise an exception so that the test fails
        raise AssertionError("ValueError was not raised when passed start node that doesn't exist")


# I also tried using unittest assertRaise to check for exceptions
# Here I am testing a case that I know will fail, and checking that an assertion was raised
class TestCases(unittest.TestCase):
    def test_end_node(self):
        data_dir = pathlib.Path(__file__).resolve().parent.parent / "data"
        graph_file = data_dir / 'citation_network.adjlist'
        G = graph.Graph(graph_file)
        self.assertRaises(ValueError, lambda: G.bfs('Martin Kampmann', 'RyanCo'))
