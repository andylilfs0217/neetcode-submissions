class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        q = [[]]

        for num in nums:
            new_q = []
            for subset in q:
                # append
                appended_subset = subset + [num]
                new_q.append(appended_subset)
                # not append
                new_q.append(subset)
            q = new_q
        return q

        