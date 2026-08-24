class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        curr_max_length = 0

        for num in nums:
            # find start num sets
            if num - 1 not in nums: 
                # loop through until we find the next num
                length = 0
                while (num + length) in nums:
                    length += 1
                
                curr_max_length = max(curr_max_length, length)
        
        return curr_max_length