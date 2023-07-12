from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        numsLen = len(nums)
        i = 0
        position = 0
        if numsLen == 1: return True
        while i < numsLen:

            position += nums[position]
            print(position)

            if position == numsLen - 1:
                return True
            elif i >= numsLen - 1:
                return False
            elif (position > numsLen - 1) or (nums[position] == 0):
                i += 1
                position = i
                print("i: ", i, "position:", position)

    def canJump(self, nums: List[int]) -> bool:
        numsLen = len(nums)
        position = 0
        jump = nums[position]
        if numsLen <= 1:
            return True
        def jumps(position,jump):
            print("position", position, "jump", jump)
            if jump > numsLen - 1: return True
            elif jump == position:
                print("Fasle")
                return
                # if position - 1 != 0:
                #     return jumps(position - 1, position - 1 + nums[position - 1])
                # else:
                #     return False
            elif nums[jump] == 0: return jumps(position,jump - 1)
            elif nums[jump] != 0:
                position += jump
                if position >= numsLen - 1:
                    print("True")
                    return True
                else:
                    jump = position + nums[position]
                    return jumps(position,jump)
            print("post position", position, "jump", jump)
        return jumps(position,jump)

    def canJump2(self, nums: List[int]) -> bool:
        numsLen = len(nums)
        position = 0
        jump = nums[position]
        if numsLen == 1: return True
        while True:
            print("position", position, "jump", jump)

            if position == numsLen - 1:
                print("1")
                return True
            elif jump == 0:
                print("2")
                return False
            elif nums[jump] != 0:
                print("3")
                position += jump
                if (position >= numsLen - 1):
                    return True
                else:
                    jump += nums[position]
            elif (jump > 0) and nums[jump] == 0:
                print("4")
                jump -= 1

    def canJump(self, nums: List[int]) -> bool:
        numsLen = len(nums)
        position = 0
        jump = nums[position]
        if numsLen <= 1:
            return True
        def jumps(position,jump):
            print("position", position, "jump", jump)
            jump = max(jump, position + nums[position])

            if jump >= numsLen - 1: return True
            elif jump == position:
                print("Fasle")
                return False
            else:
                position += 1
                if position >= numsLen - 1:
                    print("True")
                    return True
                else:
                    return jumps(position,jump)

        return jumps(position,jump)







Wynik = Solution()
nums = [2,3,1,1,4]
print("nums: ",nums)
Wynik1 = Wynik.canJump(nums= nums)
print("wynik1: ",Wynik1)

nums = [3,2,1,0,4]
print("\nnums: ",nums)
Wynik2 = Wynik.canJump(nums= nums)
print("wynik2: ",Wynik2)

nums = [0]
print("\nnums: ",nums)
Wynik3 = Wynik.canJump(nums= nums)
print("wynik2: ",Wynik3)

nums = [2,0]
print("\nnums: ",nums)
Wynik3 = Wynik.canJump(nums= nums)
print("wynik3: ",Wynik3)

nums = [3,0,8,2,0,0,1]
print("\nnums: ",nums)
Wynik4 = Wynik.canJump(nums= nums)
print("wynik4: ",Wynik4)


nums = [2,5,0,0]
print("\nnums: ",nums)
Wynik5 = Wynik.canJump(nums= nums)
print("wynik5: ",Wynik5)

nums = [5,9,3,2,1,0,2,3,3,1,0,0]
print("\nnums: ",nums)
Wynik6 = Wynik.canJump(nums= nums)
print("wynik6: ",Wynik6)