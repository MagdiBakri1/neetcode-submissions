class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        Dict_1={}
        for i in strs:
            
            H = hash("".join(sorted(i)))
            if H in Dict_1:
               Dict_1[H].append(i) 

            else:
               list_=[]
               list_.append(i) 
               Dict_1[H]= list_
        value_list = list(Dict_1.values())         
        
        
        return value_list