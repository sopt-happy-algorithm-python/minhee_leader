
def mygcd(a, b):
    L = a * b
    while b:
        a, b = b, a % b
    return L//a

for i in range(int(input())):
    a,b = map(int, input().split())
    print(mygcd(a,b))

'''
import math
import sys
t=int(input())
for _ in range(t):
    a,b=map(int,sys.stdin.readline().split())
    temp=math.gcd(a,b)
    res=a//temp
    res*=b
    print(res)
'''