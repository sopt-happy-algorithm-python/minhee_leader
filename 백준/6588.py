'''
1742년, 독일의 아마추어 수학가 크리스티안 골드바흐는 레온하르트 오일러에게 다음과 같은 추측을 제안하는 편지를 보냈다.

4보다 큰 모든 짝수는 두 홀수 소수의 합으로 나타낼 수 있다.
예를 들어 8은 3 + 5로 나타낼 수 있고, 3과 5는 모두 홀수인 소수이다. 또, 20 = 3 + 17 = 7 + 13, 42 = 5 + 37 = 11 + 31 = 13 + 29 = 19 + 23 이다.

이 추측은 아직도 해결되지 않은 문제이다.

백만 이하의 모든 짝수에 대해서, 이 추측을 검증하는 프로그램을 작성하시오.
'''

import sys

result=[]
s=[True]*1000001
for k in range(2,1000001):
    if s[k]==True:
        for j in range(k+k,1000001,k): # 배수부터 검사
            s[j]=False
    #에라토스

for k in range(2,1000001):
    if s[k]==True: #소수를 찾는다
        if s[k]!=2:
            result.append(k)
#2를제외하고 모든 소수를 result에 넣기

while True:
    T=int(sys.stdin.readline())
    if T==0:
        break
    for j in result:
        if s[T-j]: #인덱스번호랑 그거랑 같아..
            print("%d = %d + %d" % (T,j,T-j))
            break