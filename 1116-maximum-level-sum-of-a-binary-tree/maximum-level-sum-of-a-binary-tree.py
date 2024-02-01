# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        min_level, max_sum = 1, -float('inf')
        q, level = [root], 1
        while q:
            i,j = [],0
            for node in q:
                j += node.val
                if node.left:
                    i.append(node.left)
                if node.right:
                    i.append(node.right)
            if j > max_sum:
                min_level, max_sum = level, j
            q, level = i, level+1
        return min_level

        