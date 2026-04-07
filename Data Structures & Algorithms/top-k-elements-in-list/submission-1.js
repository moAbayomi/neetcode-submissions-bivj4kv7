class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
         const hash_table = {}
     const res_arr = Array.from({length: nums.length + 1}, () => [])

     for(let num of nums) {
        hash_table[num] = (hash_table[num] || 0) + 1
        
     }

     for (let [key, value] of Object.entries(hash_table)) {
        res_arr[value].push(key)
     }
     const res = []
     for (let i = res_arr.length -1; i >= 0; i--) {
        for(let num of res_arr[i]) {
            res.push(num)
            if(res.length == k) {
                return res
            }
        }
     }

    }
}
