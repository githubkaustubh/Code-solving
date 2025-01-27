#create an empty dictionary to store numbers
#loop through the list
#calculate the remaining that is target - n
#if the remaining exists then return the indices of the remaining and current number
#otherwise store the current number and its index in the dictionary




class Solution:
    def twoSum(self, nums, target):
        map = {}

        for i in range(len(nums)):
            n = nums[i]  
            remain = target - n
            
            if remain in map:
                return [map[remain], i]
            
            map[n] = i
        

        return
