class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        nums1=sorted(nums)
        nums1.remove(nums[0])
        return nums[0]+nums1[0]+nums1[1]