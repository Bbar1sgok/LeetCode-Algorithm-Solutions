class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_map = {}  
        for index, value in enumerate(nums):
            complement = target - value
            if complement in num_map:
                return [num_map[complement], index]
            num_map[value] = index
