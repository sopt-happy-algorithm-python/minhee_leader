from collections import Counter

testcase_num = int(input())
for i in range(testcase_num):
    num_card = input()
    card = list(input())
    result = Counter(card)
    first = result.most_common(2)
    if first[0][1] == first[1][1] :
        if int(first[1][0]) > int(first[0][0]):
            print("#{0} {1} {2}".format(i + 1,first[1][0],first[1][1]))
        else: print("#{0} {1} {2}".format(i + 1,first[0][0],first[0][1]))
    else :
        print("#{0} {1} {2}".format(i + 1,first[0][0],first[0][1]))
