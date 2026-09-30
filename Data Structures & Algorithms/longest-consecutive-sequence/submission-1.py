class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums=set(nums)
        longest =0
        
        for i in set_nums:
            length=1
            if i - 1 not in set_nums:
                while length+i in set_nums:
                     length+=1
            
            longest =max(length,longest)

                
                
        return longest