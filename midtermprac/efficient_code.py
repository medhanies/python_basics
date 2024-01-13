# from timeit import timeit


# nums= [1.5, 2.3, 3.4, 6.8, 3.29]

# round_nums = map(round, nums)

# print(list(round_nums))

# nums = [1,2,3,4,5]

# sqrd_nums = map(lambda x: x ** 2, nums)

# print(list(sqrd_nums)) 

# a, b = 0, 1
# # amax = 100
# L = []

# while True:
#     (a, b) = (b, a + b)
#     if a > amax:
#         break
#     L.append(a)

# print(L)

def fibonacci(N):
    L = []
    a, b = 0, 1
    while len(L) < N:
        a, b = b, a + b
        L.append(a)
    return L

# print(fibonacci(2))

def catch(*args, **kwargs):
    print("args", args)
    print("kwargs", kwargs)

# catch(1,2,3, a=5, tom=6)
# catch(4, name = 'roger')

class Solution:
    def romanToInt(self, s: str) -> int:
        return (s.count("I") + s.count("V")*5 + 
            s.count("X")*10 + s.count("L")*50 + 
            s.count("C")*100 + s.count("D")*500 +
            s.count("M")*1000 -
            s.count("IV")*2 - s.count("IX")*2 -
            s.count("XL")*20 - s.count("XC")*20 -
            s.count("CD")*200 - s.count("CM")*200
           )

x = Solution.romanToInt("C", s="CMCDDCCC")

nums = [2,7,11,15]
target = 9

# class Solution:
#     def twoSum(self, nums: 'List[int]', target: int) ->' List[int]':
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if nums[j] == target - nums[i]:
#                     return [i, j]

# x = Solution.twoSum(1, nums,target)
# print(x)

# def twoSum(nums: 'List[int]', target: int) ->' List[int]':
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if nums[j] == target - nums[i]:
#                     return [i, j]

# x = twoSum(nums, target)

# print(x)
nums = [1,1,1,2,2,3,4,5,5,5,5,6,6,6,7,8,9,9,9,9]
class Solution:
    def removeDuplicates(self, nums) -> int:   
        j = 0
        for i in range(len(nums)):
            if nums[i] != nums[j]:
                nums[j+1] = nums[i]
                j+=1
        return nums

# first = Solution.removeDuplicates([], nums)
# print(first)

def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while i < len(nums)-1:
            if nums[i] == nums[i+1]:
                del nums[i]
            else:
                i += 1
        return i+1
nums=[1,1,2,2,2,3,3,3,3,4,4,4,5]
# print(range(len(nums)))
# x = removeDuplicates([],nums)
# print(x)
import typing as t
class RemoveDuplicatesFromSortedArray:
    def removeDuplicates(self, nums: t.List[int]) -> int:
        l = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r - 1]:
                nums[l] = nums[r]
                l += 1
        return l

x = RemoveDuplicatesFromSortedArray.removeDuplicates([], nums)
print(x)

class Solution:
    def maxprofit(self, prices: t.List[int]) -> int:
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += (prices[i] - prices[i - 1])
        return profit

profit = Solution.maxprofit(1, [7, 1, 5, 3, 6, 4])
print(profit)

class Solution:
    def containsDuplicate(self, nums: t.List[int]) -> bool:
        hashset = set()
        
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False