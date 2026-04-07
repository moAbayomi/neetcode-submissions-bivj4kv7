class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
  twoSum(nums, target) {
        const hash_table = {}

        for(let i = 0; i < nums.length; i++) {
            const num = nums[i]
            hash_table[num] = i
        }

        for(let i = 0; i < nums.length; i++) {
            const num = nums[i]
            const difference = target - num

            if(difference in hash_table && hash_table[difference] != i) {
                return [i, hash_table[difference]]
            }
        }
        
    }
}
