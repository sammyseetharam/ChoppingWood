# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        self.booly = True 

        def dfs(curr): 
            
            if not curr: 
                return 0 

            leftH = dfs(curr.left)
            rightH = dfs(curr.right) 
            
            if abs(leftH - rightH) > 1:
                self.booly = False 

            return 1 + max(leftH, rightH)

        dfs(root)

        return self.booly