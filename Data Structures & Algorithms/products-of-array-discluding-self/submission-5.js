class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    
    productExceptSelf(nums) {
        const r=[]
        for(let i=0; i<=nums.length-1;i++){
            let p=1
            for(let j=0; j<=nums.length-1;j++){
                if(i==j)
                    continue
                else
                    p=nums[j]*p
            }
            r.push(p)
        }
        return r
    }
}
