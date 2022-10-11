class Solution(object):
    def targetIndices(self, nums :list[int], target :int) -> List[int]:
        ss=[]
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if nums[i]>nums[j]:
                    nums[i],nums[j]=nums[j],nums[i]
        for i in range(len(nums)):
            if nums[i]==target:
                ss.append(i)
            elif nums[i]>target:
                break
        return ss
