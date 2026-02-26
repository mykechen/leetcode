# Max heap: count frequencies, then pop k most frequent elements
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        if k == len(nums):
            return nums

        heap = []
        counter = defaultdict(int)
        res = []

        # step 1: count frequency of each number
        for n in nums:
            counter[n] += 1

        # step 2: push into max heap (negate freq since heapq is min-heap)
        for key, val in counter.items():
            heapq.heappush(heap, (-val, key))

        # step 3: pop k elements with highest frequency
        while len(res) < k:
            res.append(heapq.heappop(heap)[1])

        return res