#https://www.geeksforgeeks.org/problems/largest-subarray-with-0-sum/1

# Intiuition
# Whenever a prefix sum repeat itself means a sum of 0 is created
# Ex   - 1  3  2 -1  4 -5
# pref - 1  4  6  5  9  4
# (Over hear prefix sum 4 is repeating twice indicating subarray between those to point having resulting sum of 0)
# We will use hashmap/Dictionaries to take a remember previous prefix sum values
# A corner case we should initialize our hashmap/Dictionaries with initial sum 0
# Anytime in Future our prefix became 0 means from start to this point our total sum is 0.

class Solution:
    def maxLen(self, n, arr):
        
        lookup = {0:-1} # Value will be it's index
        pref , ans = 0 , 0
        for i in range(n):
            pref += arr[i]
            if pref in lookup:
                ans = max(ans , i - lookup[pref])
            else:
                lookup[pref] = i
        return ans