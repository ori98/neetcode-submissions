import math


class Solution:
    def total_time_to_eat(self, piles, rate):
        total_hours = 0
        # add up the ceil for all the piles
        for pile in piles:
            total_hours += math.ceil(pile / rate)

        return total_hours

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_rate = 1
        max_rate = max(piles)  # O(n)

        # we know that if the min rate works, all the rates post that work as well
        # so we binary search the first occurance of the satisfying rate
        while min_rate < max_rate:
            # find out the mid rate
            mid_rate = (min_rate + max_rate) // 2

            # then we check the total time reqd for eating (k)
            total_time_to_eat = self.total_time_to_eat(piles, mid_rate)

            # then we form cases based on total time to eat
            if total_time_to_eat <= h:
                # we need to move to the left on the line
                max_rate = mid_rate
            elif total_time_to_eat > h:
                # we need to be faster, hence move right
                min_rate = mid_rate + 1


        return max_rate
