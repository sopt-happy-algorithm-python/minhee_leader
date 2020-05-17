k = 5
if k == 1 :
    answer = '수'
if k % 2 == 0 :
    answer = '수박'*(k//2)
else :
    answer = '수'+'박수'*(k//2)


print(answer)