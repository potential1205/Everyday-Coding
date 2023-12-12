import heapq
import sys
input = sys.stdin.readline

N = int(input())

small_heap, big_heap = [],[]

for i in range(N):
    num = int(input())

    if len(big_heap) == len(small_heap):
        heapq.heappush(small_heap,-num)
    else:
        heapq.heappush(big_heap,num)
    
    if len(small_heap) >= 1 and len(big_heap) >= 1 and -small_heap[0] > big_heap[0]:
        left_val = heapq.heappop(small_heap) * -1
        right_val = heapq.heappop(big_heap)

        heapq.heappush(small_heap,-right_val)
        heapq.heappush(big_heap,left_val)

    print(-small_heap[0])


    

