# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, left, right):
            if not node:
                return True

            if not (node.val < right and node.val > left):
                return False
            
            return(
                # all value in left tree must be less than node
                # so right biundary is the value of node
                valid(node.left, left, node.val) 
                    and
                # all value in right tree must be greater than node
                # so left biundary is the value of node
                valid(node.right, node.val, right)
            )
        
        return valid(root, float('-inf'), float('inf'))