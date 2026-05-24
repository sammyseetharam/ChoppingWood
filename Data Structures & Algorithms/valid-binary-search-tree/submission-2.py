# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
    

    #my biggest miss was not keeping track globally... 

        def vally(curr, high, low):

            if not curr: 
                return True 

            if not low < curr.val < high: 
                return False 

            return vally(curr.left, curr.val, low) and vally(curr.right, high, curr.val)


        return vally(root, float('inf'), float('-inf')) 