class Solution(object):
    def intersection(self, nums1, nums2):
        result = []
        for elements in nums1:
            if elements in nums2 and elements not in result:
                result.append(elements)
        
        return result