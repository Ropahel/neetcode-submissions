class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_list = []
        while nums:
            if nums[-1] in nums_list:
                return True
            else:
                nums_list.append(nums[-1])
                nums.pop()
        return False