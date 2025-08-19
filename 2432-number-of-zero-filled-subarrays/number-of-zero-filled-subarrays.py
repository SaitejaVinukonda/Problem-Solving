class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        cnt,cns=0,0
        for i in range(len(nums)):
            if nums[i]==0:
                cns+=1
                cnt+=cns
            else:
                cns=0
        return cnt
    