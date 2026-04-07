class Solution:
    def isPalindrome(self, s: str) -> bool:
        trimmed_str = "".join([str for str in s if str.isalnum()]).lower()
        for i in range(len(trimmed_str) // 2):
            if trimmed_str[i] != trimmed_str[len(trimmed_str) - i - 1]:
                return False
        return True

        