def twoSum(self,nums:list[int],target:int)->list[int]:
    for i in range(0,len(nums)-1):
        if nums[i]+nums[i+1]==target:
            return [i,i+1]

    return [len(nums)-1,len(nums)]
