1class Solution:
2    def minimumCost(self, nums: List[int]) -> int:
3        nums1=sorted(nums)
4        nums1.remove(nums[0])
5        return nums[0]+nums1[0]+nums1[1]