class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        l, h = 0, m
        half = (m + n + 1) // 2
        total = (m + n)

        while l <= h:
            i = l + (h - l) // 2
            j = half - i

            a_left_max = nums1[i - 1] if i > 0 else float("-inf")
            a_right_min = nums1[i] if  i < m else float("inf")
            b_left_max = nums2[j - 1] if j > 0 else float("-inf")
            b_right_min = nums2[j] if j < n else float("inf")

            if a_left_max <= b_right_min and b_left_max <= a_right_min:
                if total % 2 != 0:
                    return max(a_left_max, b_left_max)
                else:
                    return (max(a_left_max, b_left_max) + min(a_right_min, b_right_min)) / 2.0
            elif a_left_max > b_right_min:
                h = i - 1
            else:
                l = i + 1



        