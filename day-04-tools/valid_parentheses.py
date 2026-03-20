class Solution:
    def isValid(self, s: str) -> bool:
        # 1. Manam matladukunna empty Stack (List)
        stack = []
        
        # 2. Meeru cheppina Dictionary mapping
        bracket_map = {')': '(', '}': '{', ']': '['}
        
        # 3. String lo unna prathi bracket ni check chesthunnam
        for char in s:
            if char in bracket_map:  # Idi closing bracket ayithe...
                # Stack lo emaina unte pop chestham, lekapothe '#' ani pedatham
                top_element = stack.pop() if stack else '#'
                
                # Pop ayina bracket, mana dictionary lo unna correct jodi kakapothe, False!
                if bracket_map[char] != top_element:
                    return False
            else:
                # Idi opening bracket ayithe, stack loki thostham (append)
                stack.append(char)
                
        # 4. Last ki stack empty ayipothe (anni perfect ga match ayyay), True return chestham. 
        # Inka emaina migilipothe, False!
        return len(stack) == 0

# Testing the code
solution = Solution()
print(solution.isValid("()"))      # Returns True
print(solution.isValid("()[]{}"))  # Returns True
print(solution.isValid("(]"))      # Returns False (Mismatch!)
print(solution.isValid("([)]"))    # Returns False (Wrong Order!)
print(solution.isValid("{[]}"))    # Returns True (Perfect nested LIFO order!)