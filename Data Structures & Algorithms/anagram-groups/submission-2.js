class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {

    const hash_map = {}

    for(let i=0; i < strs.length; i++) {
        const str = strs[i]
        const sorted_str = str.split("").sort().join("")

        if(sorted_str in hash_map) {
            hash_map[sorted_str].push(str)
        } else {
            hash_map[sorted_str] = [str]
        }
    }

    return Object.values(hash_map)


}
}
