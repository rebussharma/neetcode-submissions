# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # basically subTree must be same + same node
        # 1. find if same tree
        if not subRoot: return True
        if not root: return False
        
        return (
            self.isSameTree(root, subRoot) or
            self.isSubtree(root.left, subRoot) or
            self.isSubtree(root.right, subRoot)
        ) 

    
    def isSameTree(self, r1:Optional[TreeNode], r2:Optional[TreeNode]):
        if not r1 and not r2: return True
        if not r1 or not r2: return False
        
        return (
            r1.val == r2.val and
            self.isSameTree(r1.left, r2.left) and
            self.isSameTree(r1.right, r2.right)
        )