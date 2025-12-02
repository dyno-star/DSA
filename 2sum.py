
#Hash Map
def twoSum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

    #Brute Force
    def twoSum(num, target):
        for i in range(len(nums)):
            for j in ramge(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]