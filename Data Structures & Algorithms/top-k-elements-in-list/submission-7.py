class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dico_nums = {}

        for num in nums:
            dico_nums[f"{num}"] = 1 + dico_nums.get(f"{num}", 0)

        list_frequence = [[] for _ in range(len(nums))]

        for str_nums in dico_nums:
            if not list_frequence[dico_nums[str_nums] - 1 ]:
                list_frequence[dico_nums[str_nums] - 1] = [int(str_nums)]
            else:
                list_frequence[dico_nums[str_nums] - 1].append(int(str_nums))

        list_output = []

        for i in range(len(list_frequence)-1, -1, -1):
            if len(list_output) == k:
                return list_output
            
            if list_frequence[i]:
                for nb in list_frequence[i]:
                    list_output.append(nb)
                    if len(list_output) == k:
                        return list_output








