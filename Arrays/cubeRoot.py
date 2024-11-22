num = float(input())

def self_round(n , power):
    copy_num = n*10**(power)
    if copy_num%10 > 5:
        return (copy_num+1)/1000
    else:
        return n

def diff(mid,n):
    cube=mid*mid*mid
    if n > cube:
        return n - cube
    return cube - n

def binary_search(target,mantissa):
    ans = 0
    l,r = 0,target
    while True:
        mid = (r+l)/2
        cube=mid*mid*mid
        error = diff(mid, target)
        if error <= mantissa:
            return mid
        if cube > target:
            r = mid
        else:
            l = mid

print(round(binary_search(num , mantissa = 0.001) , 3))
