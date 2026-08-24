class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        curr_max_length = 0
        num_set = set(nums)

        for num in num_set:
            # find start num sets
            if num - 1 not in num_set: 
                # loop through until we find the next num
                length = 0
                while (num + length) in num_set:
                    length += 1
                
                curr_max_length = max(curr_max_length, length)
        
        return curr_max_length