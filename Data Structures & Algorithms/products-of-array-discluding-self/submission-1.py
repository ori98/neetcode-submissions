class Solution:
    @classmethod
    def _get_suffix_prod_arr(cls, nums: List[int]) -> List[int]:
        res_arr = [0] * len(nums)
        res_arr[len(nums) - 1] = 1

        i = len(nums) - 2

        while i >= 0:
            res_arr[i] = res_arr[i + 1] * nums[i+1]
            i -= 1
        
        return res_arr
    
    @classmethod
    def _get_prefix_prod_arr(cls, nums: List[int]) -> List[int]:
        res_arr = [0] * len(nums)
        res_arr[0] = 1

        i = 1

        while i < len(nums):
            res_arr[i] = res_arr[i - 1] * nums[i - 1]
            i += 1

        return res_arr

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        
        res_arr = [0] * len(nums)

        pref_arr = Solution._get_prefix_prod_arr(nums)
        suff_arr = Solution._get_suffix_prod_arr(nums)

        for i in range(len(nums)):
            if i == 0:
                res_arr[i] = suff_arr[i]
            elif i == len(nums) - 1:
                res_arr[i] = pref_arr[i]
            else:
                res_arr[i] = pref_arr[i] * suff_arr[i]
        
        return res_arr
        