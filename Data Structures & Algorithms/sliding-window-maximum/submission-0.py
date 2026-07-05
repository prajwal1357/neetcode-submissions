class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res=[]
        for l in range(len(nums)-k+1):
            r=k+l
            m=float('-inf')
            for i in range(l ,r):
                m=max(m, nums[i])
            res.append(m)
        return res