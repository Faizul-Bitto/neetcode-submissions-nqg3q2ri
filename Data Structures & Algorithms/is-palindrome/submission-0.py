class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanedOutput = ""

        for ch in s:
            if ch.isalnum():
                cleanedOutput += ch.lower()

        reversedString = cleanedOutput[::-1]

        return cleanedOutput == reversedString