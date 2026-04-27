class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        output = [0]*len(nums)
        prod_g_0 = 1
        count_0 = 0

        for num in nums:

            if num == 0:
                count_0 += 1

                if count_0 >= 2:
                    return output

            else:
                prod_g_0 *= num
        

        if count_0 == 0:
            for i in range(len(nums)):
                output[i] = prod_g_0 // nums[i]
        else:
            for i in range(len(nums)):
                if nums[i] == 0:
                    output[i] = prod_g_0
                else:
                    output[i] = 0       


        return output

        







