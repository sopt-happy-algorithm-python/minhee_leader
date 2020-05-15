'''
2차원 평면 위의 점 N개가 주어진다. 좌표를 x좌표가 증가하는 순으로, x좌표가 같으면 y좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.
'''
'''
list1 = [[3,4],[1,1],[1,-1],[2,2],[3,3]]
list1.sort()
print(list1)'''

import sys
n = int(sys.stdin.readline())
list1 = []
for i in range(n):
    list1.append(list(map(int, sys.stdin.readline().split())))
list1.sort()
for i in list1:
    print(i[0],i[1])