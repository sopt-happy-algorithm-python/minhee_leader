'''
왕비를 피해 일곱 난쟁이들과 함께 평화롭게 생활하고 있던 백설공주에게 위기가 찾아왔다. 일과를 마치고 돌아온 난쟁이가 일곱 명이 아닌 아홉 명이었던 것이다.

아홉 명의 난쟁이는 모두 자신이 "백설 공주와 일곱 난쟁이"의 주인공이라고 주장했다. 뛰어난 수학적 직관력을 가지고 있던 백설공주는, 다행스럽게도 일곱 난쟁이의 키의 합이 100이 됨을 기억해 냈다.

아홉 난쟁이의 키가 주어졌을 때, 백설공주를 도와 일곱 난쟁이를 찾는 프로그램을 작성하시오.
'''

import random

tall = []
for _ in range(9): tall.append(int(input()))
prime = tall[:7]
'앞에서 7개의 항목 값을 더함'
while sum(prime) != 100:
    random.shuffle(tall)
    'tall 리스트를 랜덤하게 섞어버림'
    prime = tall[:7]
    '7개 항목값 다 더함'
'랜덤하게 정렬해서 7개 더한 값이 100이 될 때까지 반복하기'
prime.sort()
for h in prime: print(h)

'''
l=[]
exec(9*'l+=[int(input())];')
'exec함수 : 문자열로 표현된 문을 인수로 받아 파이썬 컴파일 코드로 변환한다.'
l.sort()
for i in l:
	for j in l:
		if i+j==sum(l)-100:
		l.remove(i)
		l.remove(j)
for i in l:print(i)
'''
'''
<combinations 사용하기>
import sys
import itertools
short = list()
for i in range(9):
    short.append(int(sys.stdin.readline()))
s = sum(short)
for case_tuple in itertools.combinations(short,2):
    if sum(case_tuple)==s-100:
        short.remove(case_tuple[0])
        short.remove(case_tuple[1])
        break
short.sort()
for t in short:
    print(t)
    
    '''