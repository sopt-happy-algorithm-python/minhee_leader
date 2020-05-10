
testcase_num = int(input())
for i in range(testcase_num):
    num_case = input()
    temp = list(map(int,input().split()))
    print("#{0} {1}".format(i+1,max(temp) - min(temp)))
