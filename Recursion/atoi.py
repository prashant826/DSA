#https://leetcode.com/problems/string-to-integer-atoi/

# Recursion solution
class Solution:
    def myAtoi(self, s: str):

        low , high = -2**31 ,  2**31
        s = s.strip()
        n = len(s)
        def f(i):
            ans = ""
            if i >= n: return str(ans)
            if s[i] == '+' or s[i] == '-':
                if i == 0 and s[i] == '+':
                   ans += f(i+1)
                elif i == 0 and s[i] == '-':
                    ans += '-' + f(i+1)
                else:
                    return str(ans) 
            
            if s[i].isdigit():
                ans += str(s[i]) + f(i+1)
            
            return str(ans)
        ans = f(0)
        #print(ans)
        if ans == "" or ans == "-" or ans == "+":
            return 0
        elif int(ans)>=high:
            return high-1
        elif int(ans)<low:
            return low
        else:
            return int(ans)




# without recursion
# class Solution(object):
#     def myAtoi(self, s):
#         num = '0123456789'
#         res = ''
#         for x in s:
#             if x == ' ' and len(res) == 0:
#                 continue
#             if x != ' ' and (x in '-+' or x in num) and len(res) == 0:
#                 res += x
#             elif x in num:
#                 res += x
#             else:
#                 break
#         if res == '' or res in '-+':
#             return 0
#         else:
# # to avoid int casting simply run a loop and use ord(char) - ord('0')
#             if int(res) < -(2**31):
#                 return -(2**31)
#             elif int(res) > (2**31 - 1):
#                 return (2**31 - 1)
#             else:
#                 return int(res)