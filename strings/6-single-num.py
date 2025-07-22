
"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:

Input  : nums = [2,2,1]
Output : 1 

"""
class Solution(object):
    def singleNumber(self, nums):
        count = {}

        for element in nums:
            if element in count:
                count[element] += 1 
            else:
                count[element] = 1
        
        for element in nums:
            if count[element] == 1:
                return(element)
        
        """
        :type nums: List[int]
        :rtype: int
        """
        