class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        Alen = len(nums1)
        Blen = len(nums2)
        total = Alen + Blen
        half = total // 2
        i = 0
        j = 0
        nums3 = []

        while i < Alen and j < Blen:
            if A[i] <= B[j]:
                nums3.append(A[i])
                i+=1
            else:
                nums3.append(B[j])
                j+=1

        while i < Alen:
            nums3.append(A[i])
            i+=1
        
        while j < Blen:
            nums3.append(B[j])
            j+=1

        if len(nums3) % 2 == 1:
            return nums3[len(nums3) // 2]
        else:
            result = (nums3[len(nums3) // 2]  + nums3[(len(nums3) // 2) - 1]) / 2
            return result



        




        