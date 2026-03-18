class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Step 1: Clean the string (remove spaces/special chars and make lowercase)
        # This is similar to how we 'clean' text before feeding it to an LLM
        clean_s = ''.join(char.lower() for char in s if char.isalnum())
        
        # Step 2: Use Two Pointers (Left and Right)
        left, right = 0, len(clean_s) - 1
        
        while left < right:
            if clean_s[left] != clean_s[right]:
                return False
            left += 1
            right -= 1
            
        return True

if __name__ == "__main__":
    solver = Solution()
    test_str = "A man, a plan, a canal: Panama"
    print(f"Is '{test_str}' a palindrome? {solver.isPalindrome(test_str)}")