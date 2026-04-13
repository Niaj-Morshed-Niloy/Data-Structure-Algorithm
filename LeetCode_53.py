"""
53. Maximum Subarray
Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6."""


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n=len(nums)
        maxi=float("-inf")
        total=0
        for i in range(0,n):                          #Time complexity=O(N) 
            total=total+nums[i]                       #Space complexity= O(1)
            maxi=max(maxi,total)
            if total<0:
                total=0
        return maxi
