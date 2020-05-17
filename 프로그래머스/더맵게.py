import heapq
def solution(scoville, K):
    answer = 0
    heap = []
    for i in scoville:
        heapq.heappush(heap, i)
    while(min(heap)<K):
        if len(heap) == 1:
            if heap[0] < K:
                return -1
        heapq.heappush(heap, heapq.heappop(heap) + heapq.heappop(heap) * 2)
        answer+=1
    return print(answer)

sco=[1,2,3,9,10,12]
K = 7
solution(sco,K)


'''

answer = 0
sco.sort()
while(sco[0]<K):
    sco.sort()
    if len(sco) == 1:
        if sco[0] < K:
            return -1
    answer+=1
    new = sco[0]+(sco[1]*2)
    sco = sco[2:]
    sco.insert(0,new)

#print(sco)
print(answer)

'''
import heapq

def solution(scoville, K):
    answer = 0
    heap = []
    for i in scoville:
        heapq.heappush(heap, i)
    while(min(heap)<K):
        if len(heap) == 1:
            if heap[0] < K:
                return -1
        heapq.heappush(heap, heapq.heappop(heap) + heapq.heappop(heap) * 2)
        answer+=1
    return answer
