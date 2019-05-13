# Four color solver.
# Examines four-colorability for given graph.
# Time complexity O(4^C), for number of corners C.
# For documentation, license etc., see
# https://gits-15.sys.kth.se/grudat19/afage-ovn7.
# Code by Alexander Fagerlund, "afage".


def FourColorSolver():
    """Uses __GraphCreator to let user enter own graph,...
    then tries all possible colorings with function
    __Fourcolortrials."""
    first = __GraphCreator()     #can only handle connected graphs
    if __FourColorTrials(first) is True:
        print("Graph is four-colorable!")
    else:
        print("Graph is NOT four-colorable.")

class _Node:
    def __init__(self):
        self._name = None
        self._neighbors = []

class _Graph:
    def __init__(self):
        self._first = None

def __GraphCreator():
    """Tool for user to enter chosen corners...
    and links between corners."""
    graph = _Graph()
    used_node_names = []
    nodes = []
    ##########################Node names############################
    user_input = input("Provide a node name. Type '"'stop'"' at any time to finish naming nodes.")
    while user_input != "stop":
        if user_input not in used_node_names:
            new = _Node()
            new._name = user_input
            if not graph._first:
                graph._first = new
            used_node_names.append(new._name)
            nodes.append(new)
        else:
            print("Node name already in use. Be more original.")
        user_input = input("Enter new node name")
    print("Graph finished")
    ##########################Node neighbors########################
    for node in nodes:
        print("Provide new neighbor for node",node._name,". Type '"'done'"' to move on to next node.")
        inp = input()
        while inp != "done":
            while not inp in used_node_names:
                print("That node does not exist... Try again.")
                inp = input()
            if inp not in node._neighbors:
                node._neighbors.append(inp)
            if node._name in node._neighbors:
                raise ValueError("Not four-colorable as it contains self-loop!")
            print("Enter a new neighbor of",node._name)
            inp = input()
    return graph._first 

def __FourColorTrials(first):
    """Examines four-colorability of given graph Graph.
    Returns list of all corners and their colors if...
    four-colorable, otherwise returns False."""
    TruthValue = False

    return TruthValue

FourColorSolver()

