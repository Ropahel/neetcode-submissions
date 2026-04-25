class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        while nums:
            if nums[-1] in nums[:-1]:
                return True
            else:
                nums.pop()
        return False