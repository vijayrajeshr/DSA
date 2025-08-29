class Solution(object):
    def sortColors(self, nums):
        arr_0 = []
        arr_1 = []
        arr_2 = []

        for i in nums:
            if i == 0:
                arr_0.append(i)
            elif i == 1:
                arr_1.append(i)
            else:
                arr_2.append(i)

        # Combine all arrays in order to modify nums in place
        nums[:] = arr_0 + arr_1 + arr_2


# arr 0,1,2 are colors like blue,yellow,orange,red,....
#output should be like : [0 0 0 0 1 1 1 1 1 2 2 2 2 2]