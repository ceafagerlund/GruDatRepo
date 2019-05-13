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
    colors = [0,1,2,3]
    graph = _Graph()
    graph = __GraphCreator(graph)     #can only handle connected graphs
    TruthValue = True
    if __FourColorTrials(graph,colors,TruthValue) is True:
        print("Graph is four-colorable!")
    else:
        print("Graph is NOT four-colorable.")


class _Node:
    """Help class for corners in graph. Not to be tampered with."""
    def __init__(self):
        self._name = None
        self._neighbors = []
        self._color = None
        self._isVisited = False
        self._FailedColors = [False,False,False,False]
        self._FailCount = 0

class _Graph:
    """Help class for graph itself. Not to be tampered with."""
    def __init__(self):
        self._first = None
        self._members = []
        self._visited = []


def __GraphCreator(graph):
    """Tool for user to enter...
    First: chosen corners...
    Then: links between said corners."""
    used_node_names = []
    ##########################Node names############################
    user_input = input("Provide a node name. Type '"'stop'"' at any time to finish naming nodes.")
    while user_input != "stop":
        if user_input not in used_node_names:
            new = _Node()
            new._name = user_input
            used_node_names.append(new._name)
            graph._members.append(new)
        else:
            print("Node name already in use. Be more original.")
        user_input = input("Enter new node name")
    print("Graph finished")
    ##########################Node neighbors########################
    for node in graph._members:                                  # does not handle linking A to B automatically if B is linked to A
        print("Provide new neighbor for node",node._name,". Type '"'done'"' to move on to next node.")
        inp = input()
        while inp != "done":
            while not inp in used_node_names:
                print("That node does not exist... Try again.")
                inp = input()
            if inp not in node._neighbors:
                new = _Node()
                new._name = inp
                node._neighbors.append(new)
                new._neighbors.append(node)                      # Undirected graph ==> if A links to B, B has to link to A
            if inp == node._name:
                raise ValueError("Not four-colorable as it contains self-loop!")
            print("Enter a new neighbor of",node._name)
            inp = input()
    print(graph._members)
    return graph 

def __FourColorTrials(graph,colors,TruthValue):                  # Does not work yet...           
    """Examines four-colorability of given graph Graph.
    Returns list of all corners and their colors if...
    four-colorable, otherwise returns False. Uses DFS search."""
    for node in graph._members:
        if node not in graph._visited:
            print("visiting",node._name)
            if node._isVisited:
                return        
            node._isVisited = True
            node._color = colors[0]                              # Tries first color
            for neighbor in node._neighbors:                     # Compare with all neighbors
                if node._color == neighbor._color:               # If this color assignment failed...
                    for i in range(0,len(colors)):
                        if node._color == colors[i]:             # Find which color entry failed this time 
                            node._FailedColors[i] = True         # Note that that color failed
                for i in range(0,len(colors)):                   # Examine if all colors failed
                    if node._FailedColors[i] is True:
                        node._FailCount += 1                     # See if number of failed assignments is number of available assignments
                if node._FailCount == len(colors):
                    TruthValue = False                           # TruthValue is set to "False" as four-coloring fails for this node
                    break                                        # Can abandon loop, have already seen that four-coloring fails
            for neighbor in node._neighbors:                     # Recursive call
                __FourColorTrials(graph,colors,TruthValue)
    return TruthValue

FourColorSolver()

