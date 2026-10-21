class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       x = {} # map to store values as iterate through list

       for i, n in enumerate(nums): # i index in nums, n value at that index
            diff = target - n # find the difference betwen current num n and the target value

            if diff in x:
                return [x[diff], i] # checks if that diff has previously been in our list of numbers if so return index of the two
            x[n] =  i # store index of current n in map