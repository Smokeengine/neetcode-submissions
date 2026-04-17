class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        
        for i in range(len(temperatures)):
            j = i + 1

            while j < len(temperatures):
               
                if temperatures [i] < temperatures [j]:
                    res.insert(i, j-i)
                    break
                else:
                    j+=1
                     
        return res[:len(temperatures)]
        