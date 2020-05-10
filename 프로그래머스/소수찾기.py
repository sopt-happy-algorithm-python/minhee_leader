'''
1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 함수, solution을 만들어 보세요.

소수는 1과 자기 자신으로만 나누어지는 수를 의미합니다.
(1은 소수가 아닙니다.)
'''

def solution(n):
    answer = 0
    result=[]
    prime=[True]*(n+1)
    print(prime)
    for k in range(2,n+1):
        if prime[k]==True:
            for j in range(k+k,n+1,k):
                prime[j]=False
    print(prime)
    answer = prime.count(True) - 2
    return print(answer)
solution(10)

''''
def solution(n):
    num=set(range(2,n+1))

    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    return len(num)
    '''