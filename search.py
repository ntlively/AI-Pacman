# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"





    def backtrack(node):
        path = []
        while backtrack_dict[node] != "root":
            path.append(node[1])
            node = backtrack_dict[node]
        path = path[::-1]
        # print path
        return path
    frontier = util.Stack()
    initialState = (problem.getStartState() ,"none",0)
    backtrack_dict = {initialState:"root"}
    visited_dict = {initialState[0]:"root"}
    frontier.push(initialState)
    # print "frontier list",frontier.list
    if problem.isGoalState(initialState[0]): 
        return []
    while True: 
        if frontier.isEmpty():
            return False
        node = frontier.pop()
        if problem.isGoalState(node[0]):
            return backtrack(node)
        visited_dict[node[0]] = True
        for child in problem.getSuccessors(node[0]):
            if  child[0] not in visited_dict.keys():
                backtrack_dict[child] = node
                frontier.push(child)
                # print child
                # print "frontier list",frontier.list



    # global answer
    # visited = util.Stack()

    # def traversePath(current, direction, visited, path):
    #     if problem.isGoalState(current):
    #         visited.push(current)
    #         if direction!= "start":
    #             path.append(direction)
            
    #         # print "The final answer that shall be returned", path
    #         global answer
    #         answer =  path[:]
    #     else:
    #         # print "recursion works"
    #         visited.push(current)
    #         if direction!= "start":
    #             path.append(direction)
    #         for node in problem.getSuccessors(current):
    #             for trace in visited.list:
    #                 addOptions = False
    #                 if (node[0][0] == trace[0] and node[0][1] == trace[1]) == False:
    #                     # print "never visited, add to options",node
    #                     addOptions = True
    #                 else:
    #                     # print "visited before, do not add to options",node
    #                     addOptions = False
    #                     break

    #             if addOptions == True:
    #                 copy = []
    #                 copy = path[:]
    #                 print path,":", node,":",visited.list
    #                 traversePath(node[0],node[1], visited, copy)















    # currentState = problem.getStartState()

    # traversePath(currentState,"start", util.Stack(),[])

    # return answer

            


    # print "Start:", problem.getStartState()
    # print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    # print "Start's successors:", problem.getSuccessors(problem.getStartState())
    # util.raiseNotDefined()

def breadthFirstSearch(problem):

    def backtrack(node):
        path = []
        while backtrack_dict[node] != "root":
            path.append(node[1])
            node = backtrack_dict[node]
        path = path[::-1]
        # print path
        return path
    frontier = util.Queue()
    initialState = (problem.getStartState() ,"none",0)
    backtrack_dict = {initialState:"root"}
    visited_dict = {initialState[0]:"root"}
    frontier.push(initialState)
    # print "frontier list",frontier.list
    if problem.isGoalState(initialState[0]): 
        return []
    while True: 
        if frontier.isEmpty():
            return False
        node = frontier.pop()
        if problem.isGoalState(node[0]):
            return backtrack(node)
        for child in problem.getSuccessors(node[0]):
            if child not in frontier.list and child[0] not in visited_dict.keys():
                backtrack_dict[child] = node
                visited_dict[child[0]] = node[0]
                frontier.push(child)
                # print "frontier list",frontier.list
                

    
    


    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    # util.raiseNotDefined()

def uniformCostSearch(problem):

    def backtrack(node):
        path = []
        while backtrack_dict[node[0]] != "root":
            path.append(node[1])
            node = backtrack_dict[node[0]]
        path = path[::-1]
        # print path
        return path
    frontier = util.PriorityQueue()
    frontier2 = {}
    initialState = (problem.getStartState() ,"none",0)
    backtrack_dict = {initialState[0]:"root"}
    visited_dict = {}
    frontier.update(initialState,0)
    frontier2[initialState[0]] = 0
    costToGetHere = {}
    costToGetHere[initialState[0]] = 0

    while True: 
        if frontier.isEmpty():
            return False
        node = frontier.pop()
        if node[0] in frontier2.keys():
            del frontier2[node[0]]
        if problem.isGoalState(node[0]):
            return backtrack(node)
        visited_dict[node[0]] = True
        for child in problem.getSuccessors(node[0]):
            nextCost = costToGetHere[node[0]] + child[2]
            if child[0] not in visited_dict.keys() and child[0] not in frontier2.keys():
                costToGetHere[child[0]] = nextCost
                backtrack_dict[child[0]] = node
                frontier.push(child,costToGetHere[child[0]])
                frontier2[child[0]] = costToGetHere[child[0]]
            elif child[0] in frontier2.keys() and frontier2[child[0]]>child[2]:
                costToGetHere[child[0]] = nextCost
                backtrack_dict[child[0]] = node
                frontier.update(child,costToGetHere[child[0]])
                frontier2[child[0]] = costToGetHere[child[0]]


    
    # while True: 
    #     if frontier.isEmpty():
    #         return False
    #     node = frontier.pop()
    #     for child in problem.getSuccessors(node[0]):
    #         if child not in frontier.heap and child[0] not in visited_dict.keys():
    #             backtrack_dict[child] = node
    #             visited_dict[child[0]] = node[0]
    #             if problem.isGoalState(child[0]):
    #                 return backtrack(child)
    #             frontier.update(child,child[2])
    #             print frontier.heap




    #     def backtrack(node):
    #     path = []
    #     while backtrack_dict[node] != "root":
    #         path.append(node[1])
    #         node = backtrack_dict[node]
    #     path = path[::-1]
    #     print path
    #     return path
    # frontier = util.PriorityQueue()
    # initialState = (problem.getStartState() ,"none",0)
    # backtrack_dict = {initialState:"root"}
    # frontier.update(initialState,0)

    # while True: 
    #     if frontier.isEmpty():
    #         return False
    #     node = frontier.pop()
    #     if problem.isGoalState(node[0]): 
    #         return backtrack(node)
    #     backtrack_dict[node] = node
    #     for child in problem.getSuccessors(node[0]):
    #         if child not in frontier.list and child not in backtrack_dict.keys():
    #             frontier.update(child,child[2])


    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    # util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):

    def backtrack(node):
        path = []
        while backtrack_dict[node[0]] != "root":
            path.append(node[1])
            node = backtrack_dict[node[0]]
        path = path[::-1]
        # print path
        return path
    frontier = util.PriorityQueue()
    frontier2 = {}
    initialState = (problem.getStartState() ,"none",0)
    backtrack_dict = {initialState[0]:"root"}
    visited_dict = {}
    frontier.update(initialState,0)
    frontier2[initialState[0]] = heuristic(initialState[0],problem)
    costToGetHere = {}
    costToGetHere[initialState[0]] = heuristic(initialState[0],problem)

    while True: 
        if frontier.isEmpty():
            return False
        node = frontier.pop()
        if node[0] in frontier2.keys():
            del frontier2[node[0]]
        if problem.isGoalState(node[0]):
            return backtrack(node)
        visited_dict[node[0]] = True
        for child in problem.getSuccessors(node[0]):
            nextCost = costToGetHere[node[0]] + child[2]
            # if child[0] not in visited_dict.keys() and child[0] not in frontier2.keys():
            #     costToGetHere[child[0]] = nextCost
            if child[0] not in costToGetHere.keys() or nextCost < costToGetHere[child[0]]:
                costToGetHere[child[0]] = nextCost
                priority = nextCost + heuristic(child[0],problem)
                backtrack_dict[child[0]] = node
                frontier.push(child,priority)
                frontier2[child[0]] = priority
            # elif child[0] in frontier2.keys() and frontier2[child[0]]>child[2]:
            #     costToGetHere[child[0]] = nextCost
            #     priority = nextCost + heuristic(child[0],problem)
            #     backtrack_dict[child[0]] = node
            #     frontier.update(child,priority)
            #     frontier2[child[0]] = priority



    # def backtrack(node):
    #     path = []
    #     while backtrack_dict[node[0]] != "root":
    #         path.append(node[1])
    #         node = backtrack_dict[node[0]]
    #     path = path[::-1]
    #     # print path
    #     return path

    # frontier = util.PriorityQueue()
    # frontier2 = {}
    # initialState = (problem.getStartState() ,"none",0)
    # backtrack_dict = {initialState[0]:"root"}
    # frontier.update(initialState,0)
    # frontier2[initialState[0]] = 0
    # costToGetHere = {}
    # costToGetHere[initialState[0]] = 0


    # if problem.isGoalState(initialState[0]): 
    #     return []
    # while True: 
    #     if frontier.isEmpty():
    #         return False
    #     node = frontier.pop()
    #     if node[0] in frontier2.keys():
    #         del frontier2[node[0]]
    #     costToGetHere[node[0]] = node[2]
    #     for child in problem.getSuccessors(node[0]):
    #         nextCost = costToGetHere[node[0]] + child[2]
    #         if child[0] not in costToGetHere.keys() or nextCost < costToGetHere[child[0]]:
    #             costToGetHere[child[0]] = nextCost
    #             priority = nextCost + heuristic(child[0],problem)
    #             frontier.update(child, priority)
    #             frontier2[child[0]] = priority
    #             backtrack_dict[child[0]] = node
    #             if problem.isGoalState(child[0]):
    #                 return backtrack(child)




    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    # util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
