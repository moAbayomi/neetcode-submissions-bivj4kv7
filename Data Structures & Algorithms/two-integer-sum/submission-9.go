func twoSum(nums []int, target int) []int {
	hash_table := make(map[int]int)
	for i, num := range nums {
		diff := target - num
        idx, ok := hash_table[diff]
		if ok {
			return []int{idx, i}
		}
		hash_table[num] = i
	}

	return nil
}
    

