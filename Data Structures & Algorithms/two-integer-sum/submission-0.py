class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Two pointers
        i = 0
        j = 0

        # i != j
        # they must have a pair
        # i, j where i < j or j, i if j<i

        # create a set of size n 
        # Store the compliment in it 
        # we don't have the index of the original number
        # dict?
        # key -> complement, value is index

        complement_dict = dict()

        # default return value
        res = [0, 0]

        # traversal
        for i in range(0, len(nums)):
            curr_num = nums[i]
            complement = target - curr_num

            if curr_num not in complement_dict:
                # add the complement and index
                complement_dict[complement] = i
            else:
                # we return the index of original num, complement index
                res = [complement_dict[curr_num], i]
                print("res is", res)
                return res
        
        print(complement_dict)