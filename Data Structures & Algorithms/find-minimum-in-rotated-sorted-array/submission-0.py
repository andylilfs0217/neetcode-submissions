class Solution:
    def findMin(self, nums: List[int]) -> int:
        ans = nums[0]

        n = len(nums)
        l, r = 0, n-1
        while l <= r:
            m = (l+r)//2
            m_num = nums[m]
            if m_num < ans:
                ans = m_num
                r = m-1
            else:
                l = m+1

        return ans