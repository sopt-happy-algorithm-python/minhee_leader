'''
1부터 12까지의 숫자를 원소로 가진 집합 A가 있다.
집합 A의 부분 집합 중 N개의 원소를 갖고 있고, 원소의 합이 K인 부분집합의 개수를 출력하는 프로그램을 작성하시오.

해당하는 부분집합이 없는 경우 0을 출력한다. 모든 부분 집합을 만들어 답을 찾아도 된다.


예를 들어 N = 3, K = 6 경우, 부분집합은 { 1, 2, 3 } 경우 1가지가 존재한다.
'''

# 나는 모든 부분집합을 만들어서 찾는 경우의 수로 구했음!

from itertools import combinations

list_origin = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
testcase_num = int(input())

for tc in range(testcase_num):
    result = []
    count = 0
    A,B = map(int, input().split())
    c = combinations(list_origin,A)
    result.extend(c)
    for i in result:
        if sum(i) == B :
            count+=1
    print('#%s %d' % (tc+1, count))

