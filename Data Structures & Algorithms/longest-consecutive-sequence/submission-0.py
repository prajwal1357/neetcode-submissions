class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n=set(nums)
        a=[]
        for i in range(len(nums)):
            if nums[i]-1 not in n:
                a.append(nums[i])
        l=0
        for j in a:
            bl=0
            while(j in n):
                bl+=1
                if l<bl:
                    l=bl
                j+=1
        return(l)