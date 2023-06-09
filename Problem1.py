# Time Complexity : O(n) where n is the length of the given array
# Space Complexity : O(1)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# We use a fast pointer to move ahead and a slow pointer to print only 
# maximum of two occurrences of each element seen by the fast pointer.

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        l = 0
        count = 1
        for r in range(1, len(nums)):
            if nums[r] == nums[r-1]:
                count += 1
            else:
                count = 1

            if count <= 2:
                l += 1
                nums[l] = nums[r]

        return l+1