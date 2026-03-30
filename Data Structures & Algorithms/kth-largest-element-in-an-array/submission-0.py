class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        h = nums
        heapq.heapify(h)
        i = n
        while i > k:
            heapq.heappop(h)
            i -= 1
        ans = heapq.heappop(h)
        return ans