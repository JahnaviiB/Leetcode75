# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(node, depth):
            if node:
                if depth == len(j):
                    j.append(node.val)
                dfs(node.right,depth+1)
                dfs(node.left,depth+1)
        j = []
        dfs(root, 0)
        return j

        