"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        dict_cp = {}

        def dfs(curr_node: Optional['Node']) -> Optional['Node']:
            if curr_node in dict_cp:
                return dict_cp[curr_node]
            
            cp_node = Node(curr_node.val)
            dict_cp[curr_node] = cp_node

            for neighbor in curr_node.neighbors:
                cp_node.neighbors.append(dfs(neighbor))
            return cp_node

        return dfs(node)
