'''
10개의 수를 입력 받아, 그 중에서 홀수만 더한 값을 출력하는 프로그램을 작성하라.
'''

testcase_num = int(input())
for i in range(testcase_num):
    count = 0
    l = list(map(int, input().split()))
    for k in l:
        if (k % 2) != 0 : count+=k
    print("#{0} {1}".format(i + 1,count))

