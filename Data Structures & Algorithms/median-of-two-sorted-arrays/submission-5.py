class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        lenA, lenB = len(nums1), len(nums2)
        nums3 = []
        i = 0
        j = 0

        while i < lenA and j < lenB:
            if nums1[i] <= nums2[j]:
                nums3.append(nums1[i])
                i += 1
            else:
                nums3.append(nums2[j])
                j += 1
        
        while i < len(nums1):
            nums3.append(nums1[i])
            i += 1

        while j < len(nums2):
            nums3.append(nums2[j])
            j += 1

        if len(nums3) % 2 == 1:
            return nums3[len(nums3) // 2]
        result = (nums3[len(nums3) // 2] + nums3[(len(nums3) // 2) - 1]) / 2
        return result





        




        