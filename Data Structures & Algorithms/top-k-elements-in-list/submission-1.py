class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # create freq map
        freq_map = dict()
        for n in nums:
            # initialize
            if n not in freq_map.keys():
                freq_map[n] = 1
            # increment
            else:
                freq_map[n] += 1
        
        # use freq map to creat buckets
        buckets = [[] for _ in range(len(nums))]
        print("buckets", buckets)
        print("freq map", freq_map)

        # iterate freq_map to fill the buckets
        # index represent the freq and the values are the actual number
        for key, value in freq_map.items():
            buckets[value - 1].append(key)
        
        # result list
        res = []

        # iterate over the buckets to get k most freq elems
        index = len(buckets) -  1
        print(buckets)
        while index >= 0 and k > 0:
            # skip empty
            if len(buckets[index]):
                for bucket in buckets[index]:
                    res.append(bucket)
                    k -= 1
            index -= 1

        return res