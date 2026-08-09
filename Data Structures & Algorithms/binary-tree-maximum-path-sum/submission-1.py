class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = float('-inf')

        def dfs(r):
            nonlocal ans

            if r is None:
                return 0

            left = max(0, dfs(r.left))
            right = max(0, dfs(r.right))

            ans = max(ans, left + r.val + right)

            return r.val + max(left, right)

        dfs(root)

        return ans