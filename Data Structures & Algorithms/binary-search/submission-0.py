class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i=0
        j=len(nums)-1
        m=0
        while i<=j:
            m=(i+j)//2
            if nums[m] == target :
                return m
            
            if nums[m]>target:
                j=m-1
            elif nums[m] < target:
                  i = m + 1
        return -1 
        