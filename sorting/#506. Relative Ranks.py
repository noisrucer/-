class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        ranks = dict()

        sorted_score = sorted(score, reverse=True)


        for i in range(len(sorted_score)):
            if i == 0:
                ranks[sorted_score[i]] = "Gold Medal"
            elif i == 1:
                ranks[sorted_score[i]] = "Silver Medal"
            elif i == 2:
                ranks[sorted_score[i]] = "Bronze Medal"
            else:
                ranks[sorted_score[i]] = str(i + 1)
                
        for i in range(len(score)):
            if score[i] in ranks:
                score[i] = ranks[score[i]]
        
        return score