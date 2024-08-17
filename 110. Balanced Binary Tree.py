# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):
            if not root:
                return [True,0]
            leftSub = dfs(root.left)
            rightSub = dfs(root.right)
            balanced = (leftSub[0] and rightSub[0] and 
                        abs(leftSub[1] - rightSub[1]) <=1)
            return [balanced , 1+ max(leftSub[1],rightSub[1])]


        return dfs(root)[0]