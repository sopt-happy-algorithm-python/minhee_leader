height = [3, 9, 9, 3, 5, 7, 2]
answer = [0] * len(height)
for i in range(len(height)-1,0,-1):  #어쩌피 처음 숫자는 아무대도 못간다는걸 알아야
    for j in range(i-1,-1,-1):
        if (height[i] < height[j]) :
            answer[i] = j+1
            print(answer)
            break
print(answer)


