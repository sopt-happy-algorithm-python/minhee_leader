'''
10개의 수를 입력 받아, 평균값을 출력하는 프로그램을 작성하라.
'''

testcase_num = int(input())
for i in range(testcase_num):
    l = list(map(int, input().split()))
    print("#{0} {1}".format(i + 1, round(sum(l)/len(l))))


'''
실행시간 140 ms
코드길이 155 
'''