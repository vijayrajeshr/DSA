from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        target = []
        
        """
        Given an array of integers nums and an integer target,
        return indices of the two numbers such that they add up to target.

        You may assume that each input would have exactly one solution,
        and you may not use the same element twice.
        You can return the answer in any order.
        """
        for num1 in range(len(nums)):
            for num2 in range(num1+1,len(nums)):
                if num1+num2 == target:
                    return num1,num2
        
        return []