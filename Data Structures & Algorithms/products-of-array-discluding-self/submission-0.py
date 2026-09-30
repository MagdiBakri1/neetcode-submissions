class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l=[]
        n=1
        zeros =0
        for i in range(len(nums)):
            if nums[i]==0:
                zeros+=1
            else:
                n=nums[i]*n

        for i in range(len(nums)):
            if zeros==1:
                if(nums[i]==0):
                    l.append(int(n))
                else:
                    l.append(0)
            elif  zeros > 1 :
                l.append(0)
            else :
                l.append(int(n/nums[i]))
        return l

