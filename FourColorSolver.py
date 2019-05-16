# Four color solver.
# Examines four-colorability for given graph.
# Time complexity O(4^C), for number of corners C.
# For documentation, license etc., see
# https://gits-15.sys.kth.se/grudat19/afage-ovn7.
# Code by Alexander Fagerlund, "afage".


def FourColorSolver(entity,colors):
    """Main solver function.
    If user has made own graph (with __GraphCreator
    or otherwise), attempts four-coloring with function
    ColorDFS. Can only handle connected graphs.
    Returns True if four-coloring works, and raises exception otherwise.
    Exception depends on type of error, as seen below."""
    DidItWork = True
    if type(colors) is not list:
        print("not list")
        raise ValueError("color list must be LIST.")
    if type(entity) is Graph:
        if entity.First is None:
            raise ValueError("Empty graph not allowed")
        ColorDFS(entity.First,colors)
    elif type(entity) is Node:
        ColorDFS(entity,colors)
    else:
        raise ValueError("Enter a graph or a node.")
    return DidItWork                                  # Only reaches this stage if no errors (if four-coloring works)


class Node:
    """Help class for corners in graph. Not to be tampered with."""
    def __init__(self, name):
        self._name = name                              #This is a string
        self._neighbors = []
        self._color = None
        self.isVisited = False                         # To be used by ColorDFS


    def AddNeighbors(self,list):
        """Adds new neighbor to node."""
        for neighbor in list:
            if neighbor not in self._neighbors:
                self._neighbors.append(neighbor)
                neighbor._neighbors.append(self)       # Adds self to neighbor's list too




class Graph:
    """Help class for graph itself. Mostly used for help function to list members."""
    def __init__(self):
        self.Members = []
        self.First = None
        #self.CreatedWithGC = False            # Useful when applying FourColorSolver


    def PrintMembers(self):
        """Finds all elements in graph. Returns names, not memory addresses.
        Exists as user may want to return members of graph, and as helping
        function of GraphCreator."""
        for member in self.Members:
            s = ""
            s += member._name+"\t"
        return s

def GraphCreator(graph):
    """Tool for user to enter graph data.
    Requires user to have created graph object beforehand. GraphCreator then customizes graph. 
    First: chosen corners...
    Then: links between said corners.
    Program perfectly usable without this, as user
    can enter graph with instances of classes _Graph and _Node."""
    used_node_names = []
    ##########################Node names############################
    user_input = input("Provide a node name. Type '"'stop'"' at any time to finish naming nodes.")
    while user_input != "stop":
        if user_input not in used_node_names:
            new = Node(user_input)
            used_node_names.append(new._name)
            graph.Members.append(new)
            if graph.First is None:
                graph.First = new
        else:
            print("Node name already in use. Be more original.")
        user_input = input("Enter new node name")
    print("Graph finished")
    ##########################Node neighbors########################
    for node in graph.Members:                                  # does not handle linking A to B automatically if B is linked to A
        print("Provide new neighbor for node",node._name,". Type '"'stop'"' to move on to next node.")
        inp = input()
        while inp != "stop":
            while not inp in used_node_names:
                print("That node does not exist... Try again.")
                inp = input()
            if inp not in node._neighbors:
                new = Node(new)
                new._name = inp
                node._neighbors.append(new)
                new._neighbors.append(node)                      # Undirected graph ==> if A links to B, B has to link to A
            if inp == node._name:
                raise ValueError("Not four-colorable as it contains self-loop!")
            print("Enter a new neighbor of",node._name)
            inp = input()
    print("Your graph members are",graph.PrintMembers())
    return graph                                                 


def _VisitedUpdate(graph,node):
    """Updates which nodes have been visited."""
    node._isVisited = True
    graph._visited.append(node)



def TryToColor(v, Color):
    """Checks whether given color is different from all neighbors' colors.
    If so, function sets color of node to that color, as that assignment worked, and
    returns True. Else: returns False."""
    for neighbor in v._neighbors:
        if Color == neighbor._color:
            return False
    v._color = Color
    return True


def ColorDFS(v, colors):
    """Visits all nodes using DFS, and """
    if v.isVisited:
        return
    v.isVisited = True          # Marks node as visited
    _SelfLoopCheck(v)
    lastColor = colors[len(colors)-1]   # Picks out final color in list
    for color in colors:
        if TryToColor(v, color):        # If that color worked
            break
        elif color == lastColor:        # If all color assignments have failed
            raise Exception("Not four-colorable.")
    for neighbor in v._neighbors:
        ColorDFS(neighbor, colors)

def _SelfLoopCheck(node):
    """Verifies that node has no self-loop. If it has,
    node counts as its own neighbor. As node and node
    cannot possibly have different colors, graph is not four-colorable."""

    if node in node._neighbors:
        raise Exception("Not four-colorable as it contains self-loop") 

def TestException(graph,colors):
    try:
        FourColorSolver(graph,colors)
    except Exception as ex:
        return True
    return False

def TestValueError(graph,colors):
    try:
        FourColorSolver(graph,colors)
    except ValueError as ex:
        return True
    return False

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
    assert TestException(A,["red","green","blue","yellow"])     # NOT four-colorable, should not work

    F = Node("Island")
    G = Node("Izland")
    H = Node("jhdfsjfhjfhsdhj")
    F.AddNeighbors([G,H])
    G.AddNeighbors([H])
    H.AddNeighbors([F,G])
    assert FourColorSolver(F,[1,2,3,4])                         # Should work, is four-colorable
    
    a = Graph()
    assert TestValueError(a,["k","4","jhk","a"])                # Should not work, as graph is empty

    b = Graph()
    b.First = Node("node")
    b.Members.append(b.First)
    assert FourColorSolver(b,["h","kjg","kjh","jjjh"])          # Should work (trivially)

    c = Node("fgjfdgoji")
    c._neighbors.append(c)
    assert TestException(c,[1,2,3,4])                           # Should not work, as graph has self-loop

    d = Graph()
    d.First = Node("jgh")
    assert not TestValueError(d,[1,2,3,4])
