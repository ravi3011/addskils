import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        temp = []
        for i in range(len(matrix)):
            temp += matrix[i]
        res = 0
        heapq.heapify(temp)
        for i in range(k):       
            res = heapq.heappop(temp)
        return res    