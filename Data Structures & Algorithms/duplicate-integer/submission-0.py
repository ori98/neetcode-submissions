class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        storage = set()

        for num in nums:
            if num not in storage:
                storage.add(num)
            else:
                return True
        
        return False