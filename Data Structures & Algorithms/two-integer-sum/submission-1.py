class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2:
            return [0, 1]

        res = []

        # we use a dict 
        # where value -> i that we iterate through
        # key -> target - nums[i]

        #then we check if it exists in the dict

        diff_dict = {}


        for i in range(len(nums)):
            # check if this num exists in the diff_dict
            if nums[i] in diff_dict:
                return [diff_dict[nums[i]], i]
            # we realize that the dict doesn't have it
            else:
                # we add it to the dict
                diff = target - nums[i]
                diff_dict[diff] = i
