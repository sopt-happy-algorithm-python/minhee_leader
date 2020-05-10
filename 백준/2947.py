'''
동혁이는 나무 조각을 5개 가지고 있다. 나무 조각에는 1부터 5까지 숫자 중 하나가 쓰여져 있다. 또, 모든 숫자는 다섯 조각 중 하나에만 쓰여 있다.

동혁이는 나무 조각을 다음과 같은 과정을 거쳐서 1, 2, 3, 4, 5 순서로 만들려고 한다.

1)첫 번째 조각의 수가 두 번째 수보다 크다면, 둘의 위치를 서로 바꾼다.
2)두 번째 조각의 수가 세 번째 수보다 크다면, 둘의 위치를 서로 바꾼다.
3)세 번째 조각의 수가 네 번째 수보다 크다면, 둘의 위치를 서로 바꾼다.
4)네 번째 조각의 수가 다섯 번째 수보다 크다면, 둘의 위치를 서로 바꾼다.
5)만약 순서가 1, 2, 3, 4, 5 순서가 아니라면 1 단계로 다시 간다.

처음 조각의 순서가 주어졌을 때, 위치를 바꿀 때 마다 조각의 순서를 출력하는 프로그램을 작성하시오.
'''

tree = list(map(int, input().split()))
for i in range(0, len(tree)):
    for j in range(len(tree)-1):
        if tree[j] > tree[j+1] :
            tree[j], tree[j+1] = tree[j+1], tree[j]
            print(*tree)
'''
#내가 푼건데 런타임 에러ㅠ-
tree = list(map(int, input().split()))
tmp = 0
for i in range(0,5,1) :
    if tree[i] > tree[i+1] :
        tmp = tree[i]
        tree[i] = tree[i+1]
        tree[i+1] = tmp
        print(tree)

'''