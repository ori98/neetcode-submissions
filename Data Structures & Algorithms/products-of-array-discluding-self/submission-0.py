class Solution:
    def pref_prod(self, nums):
        pref_arr = [0] * len(nums)
        curr_prod = 0

        for i in range(len(nums)): 
            if i == 0:
                curr_prod = 1
            else:
                curr_prod = curr_prod * nums[i - 1]
            pref_arr[i] = curr_prod

        return pref_arr
    
    def suffix_prod(self, nums):
        suff_arr = [0] * len(nums)
        curr_prod = 0

        for i in reversed(range(len(nums))):
            if i == len(nums) - 1:
                curr_prod = 1
            else:
                curr_prod = curr_prod * nums[i + 1]
            suff_arr[i] = curr_prod

        return suff_arr

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # if it is 1 or 0 elements, return as it is
        if len(nums) <= 1:
            return nums

        pref_arr = self.pref_prod(nums)
        suff_arr = self.suffix_prod(nums)
        print(f"{pref_arr=}")
        print(f"{suff_arr=}")
        res_arr = [0] * len(nums)

        curr_prod = 1

        for i in range(len(nums)):
            if i == 0:
                curr_prod = suff_arr[0]
            elif i == len(nums) - 1:
                curr_prod = pref_arr[len(nums) - 1]
            else:
                curr_prod = suff_arr[i] * pref_arr[i]
            res_arr[i] = curr_prod
        
        return res_arr
