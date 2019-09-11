import util
from game import Directions

class SearchProblem:
    def getStartState(self):
        util.raiseNotDefined()

    def isGoalState(self, state):
        util.raiseNotDefined()

    def getSuccessors(self, state):
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

class Node:
    def __init__(self, state, path = [], priority = 0):
        self.state = state
        self.path = path
        self.priority = priority

    def __repr__(self):
        return  "({0},{1},{2})".format(self.state, self.path, self.priority)



def nullHeuristic(state, problem=None):
    return 0

def busca(problem, function, heuristic=nullHeuristic):
    closed = set()
    fringe = util.PriorityQueue()
    fringe.push(Node(problem.getStartState()), 0)
    while not fringe.isEmpty():
        node = fringe.pop()

        if problem.isGoalState(node.state):
            return node.path
        if node.state not in closed:
            closed.add(node.state)

            for successor in problem.getSuccessors(node.state):
                successor_priority = function(node.priority, successor[2])
                successor_node = Node(successor[0], node.path + [successor[1]], successor_priority)
                fringe.push(successor_node, successor_priority + heuristic(successor[0], problem))
    return []



def depthFirstSearch(problem):
    """*** YOUR CODE HERE ***"""
    return busca(problem, lambda priority, cost: priority - cost)

def breadthFirstSearch(problem):
    """*** YOUR CODE HERE ***"""
    return busca(problem,  lambda priority, cost: priority + cost)
    
def uniformCostSearch(problem):
    """*** YOUR CODE HERE ***"""
    return busca(problem,  lambda priority, cost: priority - cost)

def aStarSearch(problem, heuristic=nullHeuristic):
    """*** YOUR CODE HERE ***"""
    return generalSearch(problem, lambda priority, cost: priority + cost, heuristic)



# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch