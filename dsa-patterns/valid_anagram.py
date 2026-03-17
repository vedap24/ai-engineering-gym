class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If words length doesn't match, anagrams can't be formed.
        if len(s) != len(t):
            return False
            
        # HashMaps (Dictionaries) to store frequency of letters
        # Used HashMap to optimize time complexity to O(n) for fast retrieval.
        countS, countT = {}, {}
        
        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i], 0) + 1
            countT[t[i]] = countT.get(t[i], 0) + 1
            
        return countS == countT

if __name__ == "__main__":
    solver = Solution()
    print(f"Is 'listen' an anagram of 'silent'? {solver.isAnagram('listen', 'silent')}")
    print(f"Is 'rat' an anagram of 'car'? {solver.isAnagram('rat', 'car')}")