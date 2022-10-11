class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> List[int]::
        ls=[0]*len(nums)
        for i in range(0,len(nums)):
            for j in range(0,len(nums)):
                if nums[i] > nums[j]:
                    ls[i]+=1
                else:
                    continue
        return ls
