#https://www.geeksforgeeks.org/problems/generate-all-binary-strings/0

class Solution:
    def generateBinaryStrings(self, n):
        ans = []
        def binary_string(i, prev,curr_str):
            
            if i == n:
                ans.append(curr_str)
                return
            
            if prev == '0':
                binary_string(i+1 , '0', curr_str+ '0')
                binary_string(i+1 , '1' , curr_str + '1')
            else:
                binary_string(i+1, '0' , curr_str+'0')
        
        binary_string(0, '0', '')
        return ans