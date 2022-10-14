 class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
      
        Sum = 0
        res = 0
        dict = {0 : 1}
        
        for n in nums:
            Sum += n
            diff = Sum - k
            
            res += dict.get(diff, 0)
            dict[Sum] = 1 + dict.get(Sum, 0)
            
        return res
      
  
