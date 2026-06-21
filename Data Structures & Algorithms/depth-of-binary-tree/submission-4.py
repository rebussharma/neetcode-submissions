# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        # DFS: Traverse one side first and another
        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        
        # DFS iterative
        # pre-order: add children node, travel left subtree then right subtree
        ms = [[root, 1]]
        res = 1
        while ms:
            root, depth = ms.pop()
            if root:
                res = max(res, depth)
                ms.append([root.left, depth + 1])
                ms.append([root.right, depth + 1])
        return res
        # iterative BFS: Traverse each level, not one side first
        # level = 0
        # q = deque([root])
        # while q:
        #     for i in range(len(q)):
        #         node = q.popleft()
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
        #     level += 1
        # return level


