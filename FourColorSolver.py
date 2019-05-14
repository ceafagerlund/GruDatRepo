# Four color solver.
# Examines four-colorability for given graph.
# Time complexity O(4^C), for number of corners C.
# For documentation, license etc., see
# https://gits-15.sys.kth.se/grudat19/afage-ovn7.
# Code by Alexander Fagerlund, "afage".


def FourColorSolver(graph):
    """If user has made own graph (with __GraphCreator
    or otherwise), attempts four-coloring with function
    __4CGraph. Can only handle connected graphs."""
    colors = [0,1,2,3]
    return __4CGraph(graph,graph._first,colors)


class Node:
    """Help class for corners in graph. Not to be tampered with."""
    def __init__(self, name):
        self._name = name           #This is a string, btw
        self._neighbors = []
        self._color = None
        self.isVisited = False                         # To be used by __FourColorTrials

    def AddNeighbors(self,list):
        for neighbor in list:
            if neighbor not in self._neighbors:
                self._neighbors.append(neighbor)

class _Graph:
    """Help class for graph itself. Not to be tampered with."""
    def __init__(self):                                 #
        self._first = None
        self._members = []                              # Member list
        self._visited = []                              # Data of which nodes are visited. Use later to improve performance
        self._TruthValue = True


def __GraphCreator():
    """Tool for user to enter...
    First: chosen corners...
    Then: links between said corners.
    Program perfectly usable without this, as user
    can enter graph with instances of classes _Graph and _Node."""
    graph = _Graph()
    used_node_names = []
    ##########################Node names############################
    user_input = input("Provide a node name. Type '"'stop'"' at any time to finish naming nodes.")
    while user_input != "stop":
        if user_input not in used_node_names:
            new = Node()
            new._name = user_input
            used_node_names.append(new._name)
            graph._members.append(new)
            if graph._first is None:
                graph._first = new
        else:
            print("Node name already in use. Be more original.")
        user_input = input("Enter new node name")
    print("Graph finished")
    ##########################Node neighbors########################
    for node in graph._members:                                  # does not handle linking A to B automatically if B is linked to A
        print("Provide new neighbor for node",node._name,". Type '"'stop'"' to move on to next node.")
        inp = input()
        while inp != "done":
            while not inp in used_node_names:
                print("That node does not exist... Try again.")
                inp = input()
            if inp not in node._neighbors:
                new = Node()
                new._name = inp
                node._neighbors.append(new)
                new._neighbors.append(node)                      # Undirected graph ==> if A links to B, B has to link to A
            if inp == node._name:
                raise ValueError("Not four-colorable as it contains self-loop!")
            print("Enter a new neighbor of",node._name)
            inp = input()
    print(graph._members)
    return graph

def __4CGraph(graph,node,colors):  # Does not work yet...
    """Examines four-colorability of given graph Graph.
    Returns list of all corners and their colors if...
    four-colorable, otherwise returns False. Uses DFS search."""
    #for node in graph._members:
    if node._isVisited:
        return graph._TruthValue
    #print("Visiting node",node._name)
    _VisitedUpdate(graph,node)
    AssignColor(node,colors)                         # Find working color, update node
    if not _FailedCountCheck(graph,node,colors):
        print(node._name)
        raise Exception("You dingus, this didn't work")

    print(node._name)
    for neighbor in node._neighbors:                     # Recursive call
        __4CGraph(graph,neighbor,colors)
    #print(graph._TruthValue)
    return graph._TruthValue
def _VisitedUpdate(graph,node):
    """Updates which nodes have been visited."""
    node._isVisited = True
    graph._visited.append(node)
    
def AssignColor(node, colors):
    """Attempts color assignments for node until one works."""
    for neighbor in node._neighbors:                         # Compare with all neighbors
        if node._color == neighbor._color:                   # If this color assignment failed...
            for color in colors:
                if node._color == color:                 # Find which color entry failed this time
                    node._FailedColors[color] = True             # Note that that color failed
                    print("Color",color,"failed for",node._name)
                    if color < len(colors) - 1:
                        node._color = colors[color+1]            # Choose next available color
                        break
def _FailedCountCheck(graph,node,colors):
    """Help function to examine if all color assignments
    have failed for specific node. If that is the case,
    TruthValue is updated accordingly."""
    for i in range(0,len(colors)):                           # Examine if all colors failed
        if node._FailedColors[i] is True:
            node._FailCount += 1                             # See if number of failed assignments is number of available assignments
            print("FailCount is",node._FailCount,"for",node._name)
        if node._FailCount == len(colors):
            graph._TruthValue = False                        # TruthValue is set to "False" as four-coloring fails for this node
            return False                         # Can abandon loop, have already seen that four-coloring fails
    return True

def PrintMembers(Graph):
    for member in Graph._members:
        s = ""
        for neighbor in member._neighbors:
            s += neighbor._name+"\t"
        print(s)


def TryToColor(v, Color):
    for neighbor in v._neighbors:
        if Color == neighbor._color:
            return False
    v._color = Color
    return True


def DFS(v, colors):
    if v.isVisited:
        return
    v.isVisited = True

    lastColor = colors[len(colors)-1]
    for color in colors:
        if TryToColor(v, color):
            break
        elif color == lastColor:
            raise Exception("This didn't work")
    for neighbor in v._neighbors:
        DFS(neighbor, colors)

if __name__ == '__main__':
    # Unit test
    A = Node("Frankrike")
    B = Node("Sverige")
    C = Node("Tyskland")
    D = Node("Zimbabwe")
    E = Node("Los Espanol")
    A.AddNeighbors([B,C,D,E])
    B.AddNeighbors([A,C,D,E])
    C.AddNeighbors([A,B,D,E])
    D.AddNeighbors([A,B,C,E])
    E.AddNeighbors([B,C,D,A])
    DFS(A,["red","green","blue","yellow"])

    F = Node("Island")
    G = Node("Izland")
    H = Node("jhdfsjfhjfhsdhj")
    F.AddNeighbors([G,H])
    G.AddNeighbors([H])
    H.AddNeighbors([F,G])
    DFS(F,[1,2,3,4])
