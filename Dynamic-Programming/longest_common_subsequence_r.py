# https://practice.geeksforgeeks.org/problems/longest-common-subsequence-1587115620/1

class Solution:
    
    #Function to find the length of longest common subsequence in two strings.
    def lcs(self,x,y,s1,s2):
        
        # code here
        if x == 0 or y == 0:
            return 0
        if s1[x-1] == s2[y-1]:
            return 1 + self.lcs(x-1, y-1, s1, s2)
        else:
            return max(self.lcs(x-1, y, s1, s2), self.lcs(x, y-1, s1, s2))
