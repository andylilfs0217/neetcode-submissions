class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        for i, (x, y) in enumerate(points):
            dist = x ** 2 + y ** 2
            e = (dist, i)
            heapq.heappush(h, e)
            # if len(h) > k:
            #     heapq.heappop(h)
            
        nsmallest = heapq.nsmallest(k, h)
        ans = [points[i] for _, i in nsmallest]
        return ans