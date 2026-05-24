# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #make an array to store the entire tree in ordered value 
        #from least to greatest 

        self.arr = []

        def inOrder(root):

            if root is None:  
                return None 

            if root.left: 
                inOrder(root.left)
            
            self.arr.append(root.val)

            if root.right: 
                inOrder(root.right)

            
        inOrder(root)

        return self.arr[k-1]
            
        


            

            




            