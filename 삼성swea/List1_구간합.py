testcase_num = int(input())

for testcase_num in range(1, testcase_num+1):
    N, M = map(int, input().split())
    Data = list(map(int, input().split()))

    answer = []
    for i in range(N-M+1):
        answer.append(sum(Data[i:i+M]))
    print("#{0} {1}".format(testcase_num,(max(answer)-min(answer))))
