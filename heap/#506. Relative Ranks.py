'''
TC: O(nlogn)
SC: O(n)
'''

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        max_heap = []
        heapq.heapify(max_heap) # min-heap
        location = dict() # value: idx in score
        for idx, val in enumerate(score):
            location[val] = idx
            heapq.heappush(max_heap, -1 * val) # multiply by -1 to make max-heap
            
        rank_cnt = 1
        ranks = ['Gold Medal', 'Silver Medal', 'Bronze Medal']
        while max_heap:
            top = -1 * max_heap[0]
            heapq.heappop(max_heap)
            if rank_cnt <= 3:
                score[location[top]] = ranks[rank_cnt - 1]
            else:
                score[location[top]] = str(rank_cnt)
            rank_cnt += 1
        
        return score
            


