class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dico_nums = {}

        for num in nums:
            dico_nums[num] = 1 + dico_nums.get(num, 0)

        list_frequence = [[] for _ in range(len(nums) + 1)]

        for num in dico_nums:
            list_frequence[dico_nums[num]].append(num)

        list_output = []

        for i in range(len(list_frequence)-1, 0, -1):
            
            if list_frequence[i]:
                for nb in list_frequence[i]:
                    list_output.append(nb)
                    if len(list_output) == k:
                        return list_output








