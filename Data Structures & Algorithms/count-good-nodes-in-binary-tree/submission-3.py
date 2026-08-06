# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def dfs(r, maxv):
            nonlocal count
            if r is None:
                return
            if r.val >= maxv:
                count+=1
                maxv = max(r.val, maxv)
            dfs(r.left, maxv)
            dfs(r.right, maxv)
            return count
        

        ans = dfs(root,float('-inf'))
        return ans