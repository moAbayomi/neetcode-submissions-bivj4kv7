class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = {}
        for i, num in enumerate(nums):
            hashtable[num] = i

        for i, num in enumerate(nums):
            diff = target - num
            if diff in hashtable:
                if i != hashtable[diff]:

                    return [i, hashtable[diff]]
                



