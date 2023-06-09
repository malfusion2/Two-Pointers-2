# Time Complexity : O(m+n) where m and n are the lengths of the 2 given arrays
# Space Complexity : O(1)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

#  We start from the end 

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1, p2 = m-1, n-1
        i = m+n-1

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] >= nums2[p2]:
                nums1[i] = nums1[p1]
                p1-=1
            else:
                nums1[i] = nums2[p2]
                p2-=1
            i-=1
        
        while p2 >= 0:
            nums1[i] = nums2[p2]
            p2-=1
            i-=1
        
        return nums1
