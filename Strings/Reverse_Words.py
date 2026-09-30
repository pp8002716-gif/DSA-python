class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])


s = input("Enter a string: ")
solution = Solution()
print("Reversed words:", solution.reverseWords(s))