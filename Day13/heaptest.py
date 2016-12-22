import heapq

heap = []

heapq.heappush(heap, (3, 4))

print heap

heapq.heappush(heap, (2, 6))

print heap

heapq.heappush(heap, (1, 10))

print heap

heapq.heappop(heap)

print heap

heapq.heappush(heap, (4, 44))

print heap

heapq.heappush(heap, (2, 22))

print heap


heapq.heappop(heap)

print heap
