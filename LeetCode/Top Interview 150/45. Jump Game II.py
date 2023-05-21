from typing import List
class Solution:
    def jump(self, nums: List[int]) -> int:
        numsLen = len(nums)
        position = 0
        jump = nums[position]
        jumpsNumber = 1

        if numsLen <= 1:
            return 0
        elif jump >= numsLen - 1:
            return 1
        def jumps(position,jump,jumpsNumber):
            rangeStart = jump
            rangeStop = position
            for i in range(rangeStart,rangeStop,-1):

                if i > numsLen - 1:
                    i = numsLen - 1

                if i + nums[i] >= jump:
                    jump = i + nums[i]
                    position = i
                print("i: ", i, " jump:",jump ," i + nums[i]:", i + nums[i])

            print("position", position, "jump", jump, " jumpsNumber:", jumpsNumber)

            if jump >= numsLen - 1:
                # jumpsNumber += 1
                print("if")
                if position == 0:
                    return jumpsNumber
                else:
                    return jumpsNumber + 1
            elif jump == position:
                print("Fasle")
                return 0
            else:
                print("else")
                jumpsNumber += 1
                if position >= numsLen - 1:
                    print("True")
                    return jumpsNumber
                else:
                    return jumps(position,jump,jumpsNumber)

        return jumps(position,jump,jumpsNumber)







Wynik = Solution()
nums = [2,3,1,1,4]
print("nums: ",nums)
Wynik1 = Wynik.jump(nums= nums)
print("wynik1: ",Wynik1)

nums = [3,2,1,0,4]
print("\nnums: ",nums)
Wynik2 = Wynik.jump(nums= nums)
print("wynik2: ",Wynik2)

nums = [0]
print("\nnums: ",nums)
Wynik3 = Wynik.jump(nums= nums)
print("wynik2: ",Wynik3)

nums = [2,0]
print("\nnums: ",nums)
Wynik3 = Wynik.jump(nums= nums)
print("wynik3: ",Wynik3)

nums = [3,0,8,2,0,0,1]
print("\nnums: ",nums)
Wynik4 = Wynik.jump(nums= nums)
print("wynik4: ",Wynik4)


nums = [2,5,0,0]
print("\nnums: ",nums)
Wynik5 = Wynik.jump(nums= nums)
print("wynik5: ",Wynik5)

nums = [5,9,3,2,1,0,2,3,3,1,0,0]
print("\nnums: ",nums)
Wynik6 = Wynik.jump(nums= nums)
print("wynik6: ",Wynik6)

nums = [1,2]
print("\nnums: ",nums)
Wynik6 = Wynik.jump(nums= nums)
print("wynik6: ",Wynik6)
