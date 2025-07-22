class Solution(object):
    def twoSum(self, nums, target):

        # Step 1: Create an empty dictionary
        # We'll store {number: index}
        seen = {}

        # Step 2: Loop through the list of numbers
        for i in range(len(nums)):
            num = nums[i] 

# current number we're looking at
            # x + y = target
            # num + diff = target
            diff = target - num         
# what number would we need to make target?

           
 # Step 3: Check if that needed number (diff) was already seen
            if diff in seen:
# if yes, we've found a pair: return the indices
                return [seen[diff], i]

# Step 4: If not found, store this number with its index for later
            seen[num] = i


