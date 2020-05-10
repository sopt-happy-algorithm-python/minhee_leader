
def find_st(p, cnt):
    temp=[]
    if p+R>=N: #이동하는게 마지막 도착에 걸리지만
        return p,cnt #걸리면 마지막으로 가는거니깐 바로 출력
    else: #도착 못하는거
        cnt+=1
        chk=0
        for X in range(p+1, p+R+1):#p+1 : 바로다음정류장부터 p+R+1 : 세번째이상
            if list_n[X]: #여기충전기가 있나요?
                temp.append(X) #충전한 노선을 temp에 저장
                chk+=1
        if chk==0:
            return N,0

        return find_st(temp[-1],cnt)

for i in range(int(input())):
    R, N, C=map(int, input().split(' '))
    cnt=0
    M=list(map(int,input().split(' ')))
    list_n=[int(i in M) for i in range(N+1)]
    #list_n은 충전기가 있는 노선은 1, 없으면 0으로 배열해둔 리스
    P=find_st(0,0)[1]
    print('#{}'.format(i+1),P)


'''
<효원언니코드>
T = int(input())
for k in range(T):
    K, N, M = map(int, input().split())
    a = list(map(int, input().split())) #충전기 위치
    M_list = [0] * (N + 1) #정류장
    for i in range(len(a)):
        M_list[a[i]] += 1 #충전기 있는 정류장은 1로 변경
    count = 0
    start = 0
    end = K
#이제 a리스트는 쓸모 없음 합쳐서
#내가 가지고있는 범위에가 가장 먼 충전기에서 충전..
    while True:
        zero = 0
        for j in range(start + 1, end + 1): #층전할때마다
            if M_list[j] == 1:
                start = j #한번간곳으로 start위치를 변경해
            else:
                zero += 1 #기회를 깎고있다.
        if zero == K: #충전기 설치가 잘못되어 종점에 도착할 수 없는 경우
            count = 0
            break

        count += 1
        end = start + K

        if end >= N:
            break

    print("#%d %d" % (k + 1, count))
'''