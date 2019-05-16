# FourColorCutouts

#def __4CGraph(graph,node,colors):  # Does not work yet...
#    """Examines four-colorability of given graph Graph.
#    Returns list of all corners and their colors if...
#    four-colorable, otherwise returns False. Uses DFS search."""
#    #for node in GraphMembers:
#    if node._isVisited:
#        return graph._TruthValue
    #print("Visiting node",node._name)
#    _VisitedUpdate(graph,node)
#    AssignColor(node,colors)                         # Find working color, update node
#    if not _FailedCountCheck(graph,node,colors):
#        print(node._name)
#        raise Exception("You dingus, this didn't work")

#    print(node._name)
#    for neighbor in node._neighbors:                     # Recursive call
#        __4CGraph(graph,neighbor,colors)
    #print(graph._TruthValue)
#    return graph._TruthValue



#def AssignColor(node, colors):
#    """Attempts color assignments for node until one works."""
#    for neighbor in node._neighbors:                         # Compare with all neighbors
#        if node._color == neighbor._color:                   # If this color assignment failed...
#            for color in colors:
#                if node._color == color:                 # Find which color entry failed this time
#                    node._FailedColors[color] = True             # Note that that color failed
#                    print("Color",color,"failed for",node._name)
#                    if color < len(colors) - 1:
#                        node._color = colors[color+1]            # Choose next available color
#
#                        break

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
