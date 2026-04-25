class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums) - 1):
            if nums[i] in nums[i+1:]:
                return True
        return False