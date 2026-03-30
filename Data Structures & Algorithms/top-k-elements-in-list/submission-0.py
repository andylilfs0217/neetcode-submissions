class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        counter = Counter(nums)
        max_count = max(counter.values())
        buckets = [[] for _ in range(max_count+1)]
        for num, count in counter.items():
            buckets[count].append(num)
        result = list()
        for count in range(max_count, -1, -1):
            nums_in_bucket = buckets[count]
            nums_nums = len(nums_in_bucket)
            result.extend(nums_in_bucket)
            k -= nums_nums
            if (k <= 0):
                break
        return result