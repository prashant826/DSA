# https://www.geeksforgeeks.org/problems/max-sum-in-sub-arrays0824/0?category&utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=max-sum-in-sub-arrays

class Solution:
    def pairWithMaxSum(self, arr, N):
        
        # Your code goes here
        maxi = -float('inf')
        for i in range(1,N):
            
            maxi = max(maxi , arr[i]+arr[i-1])
        return maxi