"""
from hashlib import new
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        clones = {}

        def dfs(node): 
            if node in clones: #avoid cycle as it catches when it has already been found 
                return clones[node]

            #creates a new node and then finds its neighbors 
            newNode = Node(node.val)
            clones[node] = newNode
            for n in node.neighbors:  
                newNode.neighbors.append(dfs(n))

            return newNode

        if node: 
            return dfs(node)
        
        return None 
