# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, maxy):
            if not root: 
                return 0 

            count = 0

            if root.val >= maxy: 
                count = 1 

            newMax = max(maxy, root.val)

            count += dfs(root.left, newMax)
            count += dfs(root.right, newMax)

            return count 
            
        
        return dfs(root, root.val)

