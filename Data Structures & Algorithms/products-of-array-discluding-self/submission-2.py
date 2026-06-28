class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        r=[]
        for i in range(len(nums)):
            p=1
            for j in range(len(nums)):
                if i==j:
                    continue
                else:
                    p=nums[j]*p
            r.append(p)
        return(r)