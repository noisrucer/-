class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        poisoned = duration

        for i in range(len(timeSeries)-1):
            if timeSeries[i + 1] - timeSeries[i] < duration:
                poisoned += timeSeries[i + 1] - timeSeries[i]
            else:
                poisoned += duration

        return poisoned
    
    
'''
원래 중독되야하는 시간이 duration 만큼인데 만약 
time[i + 1] - time[i] < duration이 해당 시간에 중독 되는 시간이 겹친다(짧아진다)는 의미니까
그 시간만큼 빼주고 원래 중독시간만큼 더해줌

'''