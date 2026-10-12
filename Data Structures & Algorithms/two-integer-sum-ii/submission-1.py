class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lift =0
        right=len(numbers)-1

        while lift < right:
            sum = numbers[lift]+numbers[right]
            if sum>target:
                right-=1
            elif sum<target:
                lift+=1
            else:
                return [lift+1,right+1]