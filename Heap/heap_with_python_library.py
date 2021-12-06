from heapq import heappop, heappush, heapify

nums = [15, 35, 10, 11, 5, -2, -25, 100, 500, 10000, -200, 23]

heap = []

for num in nums:
    heappush(heap, num)

print("Pooping heap item:")

while heap:
    print(heappop(heap))

print("heapify library: ")
heapify(nums)
print(nums)