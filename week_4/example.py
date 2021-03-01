
import heapq # heapq 를 사용하기 위해서는 맨 위에 heapq 를 가져온다! 라는 구문을 써주셔야 합니다.

heap = []
heapq.heappush(heap, 4)
heapq.heappush(heap, 1)
heapq.heappush(heap, 7)
heapq.heappush(heap, 3)
print(heap)
[1, 3, 7, 4] # 힙의 형태를 유지한채로 원소가 넣어지기 때문에 heap[0]이 최솟값입니다!

print(heapq.heappop(heap)) # 최솟값을 빼는 방법입니다.
1
print(heap)
[3, 7, 4] # 마찬가지로 힙의 형태가 유지됩니다.
