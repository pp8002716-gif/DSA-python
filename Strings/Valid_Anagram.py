class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


s = input("Enter first string: ")
t = input("Enter second string: ")

solution = Solution()

if solution.isAnagram(s, t):
    print("Valid Anagram")
else:
    print("Not a Valid Anagram")