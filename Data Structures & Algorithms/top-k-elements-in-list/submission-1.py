import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        queue = []
        for num, count in counter.items():
            heapq.heappush(queue, [-count, num])
        ans = []
        for i in range(k):
            _, num = heapq.heappop(queue)
            ans.append(num)
        return ans