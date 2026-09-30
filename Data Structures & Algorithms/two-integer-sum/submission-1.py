class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i, item in enumerate(nums):
            
            for j, item in enumerate(nums):
                if i!=j:
                   

                    if nums[i] + nums[j]== target:
                        Output=[]
                        Output.append(i)
                        Output.append(j)
                        return Output



        