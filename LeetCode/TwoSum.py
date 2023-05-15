from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    print("List lenght: ",len(nums))
    i = 0
    while i < len(nums):

        for l in nums:
            if l > i:
                if (l + (l - i) == target) and (l != (l - i)):
                    print("Znalazło parę:", [l - i,l])
                    return [l - i,l]
        i += 1

x = twoSum([3,4,5,6,7],10)
print(x)