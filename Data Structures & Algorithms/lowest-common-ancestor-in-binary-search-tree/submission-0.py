# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #need to take advantage of the fact its a BST 
        #so that means all lowers are in the left and all uppers in the right

        #if curr > p and q go left 
        if root.left and (root.val > p.val and root.val > q.val): 
            return self.lowestCommonAncestor(root.left, p, q)

        #if curr < p and < q
        if root.right and (root.val < p.val and root.val < q.val): 
            return self.lowestCommonAncestor(root.right, p, q)

        #if curr > p and < q or either way like that curr is the lowestCommonAncestor            
        return root 
            
        
