#https://www.geeksforgeeks.org/problems/perfect-sum-problem5633/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=perfect-sum-problem

# recursive approach time complexity - O(2^N) space complexity - O(N)
class Solution:
    def perfectSum(self, arr, n, sum): 
        mod = 1000*1000*1000+7
        arr.sort()

        def Count(i, curr):
	        
            if i >= n:
                return int(curr == 0)
            
            pick=0
            if arr[i] <= curr:
                pick = Count(i+1, curr -arr[i])%mod
            notPick = Count(i+1, curr)%mod
            return (pick + notPick)%mod
        
        return Count(0 , sum)


# recursive + Memoization time complexity - O(N*sum) space complexity - O(N*sum)
# class Solution:
#     def perfectSum(self, arr, n, sum): 
#         mod = 1000*1000*1000+7
#         arr.sort()
#         dp = [[-1 for _ in range(sum+1)] for _ in range(n+1)]
#         def Count(i, curr):
	        
#             if i >= n:
#                 return int(curr == 0)
            
#             if dp[i][curr] != -1:
#                 return dp[i][curr]
            
#             pick=0
#             if arr[i] <= curr:
#                 pick = Count(i+1, curr -arr[i])%mod
#             notPick = Count(i+1, curr)%mod
#             dp[i][curr] = (pick + notPick)%mod
#             return dp[i][curr]
        
#         return Count(0 , sum)