
'''
이해가 안감.. ㅠㅠ 설명해줄사람

'''
testcase_num = int(input())
for tc in range(1, testcase_num+1):
    N = int(input())
    red = []
    blue = []
    for i in range(N):
        x1, y1, x2, y2, color = map(int, input().split())
        for y in range(y1, y2+1):
            for x in range(x1, x2+1):
                if color == 1:
                    red.append((y,x))
                elif color == 2:
                    blue.append((y,x))

    result = []
    if len(red) > len(blue):
        for i in blue:
            if i in red:
                result.append(i)

    if len(red) < len(blue):
        for i in red:
            if i in blue:
                result.append(i)

    print('#%s %d'%(tc, len(result)))