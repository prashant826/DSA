#https://leetcode.com/problems/generate-parentheses/

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        def gen_param(open, close , curr):
            
            if open == n  and close == n:
                res.append(curr)
                return
            if open<n:
                gen_param(open+1, close, curr + '(')
            if close < open:
                gen_param(open, close+1,curr+')')
        gen_param(0, 0 , '')
        return res