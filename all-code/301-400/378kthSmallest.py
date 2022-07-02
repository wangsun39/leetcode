import heapq
class Solution:
    def kthSmallest(self, matrix, k):
        n = len(matrix)
        heap = []
        valid_line = [i for i in range(n)]
        for column in range(n):
            t = []
            for row in valid_line:
                if len(heap) < k:
                    heapq.heappush(heap, -matrix[row][column])
                    min_num = heap[0]
                else:
                    if -matrix[row][column] > min_num:
                        heapq.heappop(heap)
                        heapq.heappush(heap, -matrix[row][column])
                        min_num = heap[0]
                    else:
                        t.append(row)
            valid_line = list(set(valid_line) - set(t))
        return -heapq.heappop(heap)

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
]
k = 8



so = Solution()
#print(so.findKthLargest([3,2,1,5,6,4], 2))
#print(so.findKthLargest([3,2,3,1,2,4,5,5,6], 4))
#print(so.findKthLargest([7,6,5,4,3,2,1], 5))
print(so.kthSmallest(matrix, k))

