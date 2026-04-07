class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hash = {}
        freq_arr = [[] for i in range(len(nums) + 1)]

        for num in nums:
            hash[num] = hash.get(num, 0) + 1

        for key, value in hash.items():
            freq_arr[value].append(key)

        res = []

        for i in range(len(freq_arr) - 1, 0, -1):
            for n in freq_arr[i]:
                res.append(n)
                if len(res) == k:
                    return res
        