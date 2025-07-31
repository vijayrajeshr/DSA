class Solution:
    def segregateElements(self, arr):
        # Your code goes here
        pos_arr = []
        neg_arr = []
        
        for num in arr:
            if num>0:
                pos_arr.append(num)
            else:
                neg_arr.append(num)
        #this line is 
        out_arr = pos_arr + neg_arr
        for i in range(len(arr)):
            arr[i] = out_arr[i]
