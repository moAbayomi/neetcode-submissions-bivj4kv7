class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hash_map = {}
        for i, num in enumerate(numbers):
            hash_map[num] = i

        for i in range(len(numbers)):
            num = numbers[i]
            diff = target - num
            if diff in hash_map and i != hash_map[diff]:
                return [i + 1, hash_map[diff] + 1]
        return []
        
        