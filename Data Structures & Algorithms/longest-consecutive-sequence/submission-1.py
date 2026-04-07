class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest_seq = []
        for i in range(len(nums)):
            output = 0
            curr = nums[i]
            if (curr - 1) not in num_set:
                output += 1
                while (curr + 1) in num_set:
                    output+=1
                    curr += 1
            longest_seq.append(output)

        if len(longest_seq) < 1: 
            return 0
        return max(longest_seq)

        
