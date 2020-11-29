import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashTable = dict()
        for e in nums:
            if(e in hashTable):
                hashTable[e] += 1
            else:
                hashTable[e] = 1
                
        temp = []        
        for key,value in hashTable.items():
            heapq.heappush(temp,[value,key])
        # heapq.heapify(temp)
        res = []
        for _,v in heapq.nlargest(k,temp):
            res.append(v)
        return res 