class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res


    def decode(self, s: str, res = None) -> List[str]:

        if res is None:
            res = []

        if not s:
            return res
    
        j = 0
        while s[j] != "#":
            j = j + 1
        length_of_str = int(s[:j])
        start_of_string = j+1
        end_of_string = start_of_string + length_of_str
        res.append(s[start_of_string:end_of_string])

        return self.decode(s[end_of_string:], res)
