#https://leetcode.com/problems/count-good-numbers/
#https://cp-algorithms.com/algebra/binary-exp.html

# additional topic biniary exponentiation (advance number theory) is required to solve the problem

#return 100
# even prime even
# 5 4 5 = 100
# odd number 5**2 * even number of 4**2
# n//2        

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 1000*1000*1000+7

        def pow(a, b):
            a %=mod
            res = 1
            while b > 0:
                if b&1:
                    res = (res*a)%mod
                a = (a*a)%mod
                b = b >> 1
            return res
        
        odd_power = (n+1)//2
        even = n//2
        return (pow(4, even)*pow(5,odd_power))%mod