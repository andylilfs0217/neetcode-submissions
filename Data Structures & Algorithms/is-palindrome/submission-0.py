class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = list()
        for char in s:
            if char.isalnum():
                lower_char = char.lower()
                chars.append(lower_char)
        n = len(chars)
        for i in range(n//2):
            j = n-1-i
            if chars[i] != chars[j]:
                return False


        return True
