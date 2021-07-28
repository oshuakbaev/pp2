class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        a = {}
        res = 0
        for i in nums:
            if not i in a:
                a[i] = 0
            a[i] += 1
        for i in a:
            n = a[i]
            res += (n * (n - 1) // 2)
        return res
