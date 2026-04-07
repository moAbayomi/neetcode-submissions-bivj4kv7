import "slices"

func sort_str(s string)string {
	 runes := []rune(s)
    slices.Sort(runes) 
    return string(runes)
}

func groupAnagrams(strs []string) [][]string {
	hash := make(map[string][]string)
	res := [][]string{}

	for i:= 0; i < len(strs); i++ {
		str := strs[i]
		sorted_str := sort_str(str)

		hash[sorted_str] = append(hash[sorted_str], str)
	}

	for _, val := range hash {
		res = append(res, val)
	}

	return res
}