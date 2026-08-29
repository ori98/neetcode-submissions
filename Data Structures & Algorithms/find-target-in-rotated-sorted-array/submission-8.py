class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        left_ptr = 0
        right_ptr = n - 1


        while left_ptr <= right_ptr:
            mid_ptr = (left_ptr + right_ptr) // 2

            if target == nums[mid_ptr]:
                # happy
                return mid_ptr
            
            # if left half is sorted
            elif nums[left_ptr] <= nums[mid_ptr]:
                if nums[left_ptr] <= target and target < nums[mid_ptr]:
                    # it is in sorted half
                    right_ptr = mid_ptr - 1
                # else target is in unsorted half
                else:
                    left_ptr = mid_ptr + 1
            # if right half is sorted
            else:
                if nums[mid_ptr] < target and target <= nums[right_ptr]:
                    # target in sorted half
                    left_ptr = mid_ptr + 1
                else:
                    # target in unsorted left half
                    right_ptr = mid_ptr - 1
        
        # not found
        return - 1