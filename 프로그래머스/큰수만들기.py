def solution(number, k):
    list_k = []
    # 일단 먼저 제일 큰 게 앞으로 온 후 쌓이는 형태
    for i, j in enumerate(number):
        print("i와 j:",i,j)
        print("k는 ",k)
        while len(list_k) > 0 and list_k[-1] < j and k > 0:  #그 다음수가 나보다 큰지 비교
        # 1. len(list_k)>0은 맨 처음에 무조건 넣 고 시작하려고 넣음
        # 2. list_k[-1] < j는 맨 위에 인덱스와 이제 넣을 인덱스를 비교하기 위해 넣음
        # 3. k > 0 는 몇개를 제거하는지 보는것
            list_k.pop()
            k -= 1
        list_k.append(j)
        print(list_k)
    if k!=0:
        list_k = list_k[:-k]
    return print(''.join(list_k))
solution("1924",2)


