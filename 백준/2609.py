'''
두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.
'''

from math import gcd
def less(a,b) :
    return a*b // gcd(a,b)
A,B = map(int,input().split())
print(gcd(A,B),less(A,B),sep="\n")

'''
a, b = map(int, input().split())

L = a*b
while b:
    a, b = b, a%b

print(a, L//a)
'''