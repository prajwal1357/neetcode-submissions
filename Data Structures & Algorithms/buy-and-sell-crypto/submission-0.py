class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m=[]
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if prices[i]<prices[j]:
                    m.append(prices[j]-prices[i])
        return max(m) if m else 0 