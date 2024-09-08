#https://www.geeksforgeeks.org/problems/reverse-a-stack/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=reverse-a-stack
 
class Solution:
    
    def reverse(self,St):
        
        if len(St) == 0:
            return
        ele = St.pop(0)
        Solution.reverse(self, St)
        St.append(ele)