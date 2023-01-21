'''Method 1 - Greedy
TC: O(n)
SC: O(1)
'''
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        n = len(nums)
        for i in range(n):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + nums[i])

        return True


'''Method 2 - Greedy (backwards)
TC: O(n)
SC: O(1)
'''

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dest = n - 1
        
        for i in range(n-2, -1, -1):
            if i + nums[i] >= dest:
                dest = i
                
        return dest == 0
    
    
''' Method 3 - DP
- TLE
'''

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        self.nums = nums
        self.n = len(nums)
        dp = [-1 for _ in range(self.n)]
        return self.topdown(0, dp)
        # f(i) = whether it can reach to last index from i
        # f(i) = || f(i + x)
        
    def topdown(self, i, dp):
        if i == self.n - 1:
            return True
        
        if i >= self.n:
            return False
        
        if self.nums[i] == 0 and i < self.n - 1:
            return False
        
        if dp[i] != -1:
            return dp[i]
        
        possible = 0
        for jump in range(1, self.nums[i] + 1):
            possible = possible or self.topdown(i + jump, dp)
            if possible:
                break
            
        dp[i] = possible
        return dp[i]