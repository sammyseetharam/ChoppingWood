# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #it just takes one case to break it right 
        #solution is obv recursive DFS here and to compare heights of 
        #both left and right sides for each 
        #I want to store the right and left heights at each curr node

        self.lH, self.rH = 0, 0
        self.booly = True

        if not root: 
            return True
        
        def dfsL(curr): 
            if not curr:  
                return 0

            leftH = dfsL(curr.left)
            self.lH = leftH
            rightH = dfsL(curr.right)
            self.rH = rightH


            if abs(leftH - rightH) > 1: 
                self.booly = False

            return 1 + max(leftH, rightH)

        dfsL(root)

        return self.booly

        