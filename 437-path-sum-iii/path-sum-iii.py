# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, node: Optional[TreeNode], targetSum: int) -> int:
        self.count = 0
        def helper(node,num):
            if not node:
                return 0
            if num + node.val == targetSum:
                self.count += 1
            num += node.val
            helper(node.left, num)
            helper(node.right,num)

        def dfs(node):
            if not node:
                return 0
            helper(node,0)
            dfs(node.left)
            dfs(node.right)
        dfs(node)
        return self.count
        