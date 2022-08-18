# 7) OPTIONAL STEP (up to 15 points extra credit): In programming assignment 2, you
#    implemented a parser for some
#    highway graph data files.  Implement another python module (i.e., another .py file)
#    with an if main block where you: (a) get a highway graph filename from the
#    command line, (b) use your parser from assignment 2 to get a WeightedGraph (you'll
#    need an import statement for your parser), and (c) use either Bellman Ford or
#    Dijkstra to compute the Single Source Shortest Paths for the source vertex of
#    your choice.

import graphfileparser
from timeit import timeit
import sys

def getHighwayTime(filename):
    numRuns = 10

    print("Graph Num | BellmanFord |   Dijkstra   |")
    i = 0

    graph = graphfileparser.parseHighwayGraphFile(filename)
    """Generates a table of timing results comparing Dijkstra and Bellman-Ford."""
    t1 = timeit(lambda: graph.bellmanFord(0), number=numRuns)
    t2 = timeit(lambda: graph.dijkstra(0), number=numRuns)

    print(" Graph", i + 1, '{: >2}'.format("|"), '{0:.8f}'.format(t1 / numRuns), " | ", '{0:.8f}'.format(t2 / numRuns), " |")



if __name__ == "__main__":
    p = 0
    i=0
 # this is the counter to ensure that the correct arg is used (I tried it withp
    for arg in sys.argv:
        if i != 0:
            getHighwayTime(sys.argv[i])
            i = i + 1

        if i == 0:
            i = i + 1