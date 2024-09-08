# https://leetcode.com/problems/subsets/

# recursion solution

class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        res = []
        def sub(i , curr):

            if i == n:
                res.append(curr)
                return
            sub(i+1 , curr)
            sub(i+1, curr + [nums[i]])
        sub(0,[])
        return res

# bitwise solution
# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
        
#         n = len(nums)
#         k = 1<<n
#         res = []
#         for i in range(k):
#             ans = []
#             for j in range(n):
#                 if i&(1<<j):
#                     ans.append(nums[j])
#             res.append(ans)
#         return res