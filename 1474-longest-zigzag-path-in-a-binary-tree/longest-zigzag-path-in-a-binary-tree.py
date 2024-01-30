# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.count = 0

        def dfs(node, goright, i):
            if node:
                self.count = max(self.count, i)

                if goright:
                    dfs(node.right, False, i+1)
                    dfs(node.left, True,1)
                else:
                    dfs(node.right,False,1)
                    dfs(node.left, True, i+1)
        dfs(root,False,0)
        dfs(root,True,0)
        return self.count
        