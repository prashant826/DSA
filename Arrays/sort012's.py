class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        l , r = 0, n-1
        i = 0

        for i in range(n):

            while i>=l and i<=r and (nums[i] == 0 or nums[i] == 2):
                
                if nums[i] == 0:
                    nums[i], nums[l] = nums[l] , nums[i]
                    l+=1
                elif nums[i] == 2:
                    nums[i], nums[r] = nums[r], nums[i]
                    r-=1