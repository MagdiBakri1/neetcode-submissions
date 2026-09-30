class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        D= {}

        for i in nums:
            
            if i in D:
                D[i]+=1
            else:
                D[i]=1
        D = dict(sorted(D.items(), key=lambda item: item[1], reverse=True))
       
        list_=[]
        for key, value in D.items():
            list_.append(key)

        return list_[0:k]
        