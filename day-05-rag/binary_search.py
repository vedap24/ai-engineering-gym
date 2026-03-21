from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 1. Starting and Ending pointers
        left = 0
        right = len(nums) - 1
        
        # 2. Loop until the search space is exhausted
        while left <= right:
            # 3. Meeru cheppina Floor Division (//) vadutunnam!
            mid = (left + right) // 2
            
            # 4. Target dorikeste, direct ga index return chestham
            if nums[mid] == target:
                return mid
                
            # 5. Target peddadi ayithe, right side vethukutham (left ni jaruputham)
            elif nums[mid] < target:
                left = mid + 1
                
            # 6. Target chinnadi ayithe, left side vethukutham (right ni jaruputham)
            else:
                right = mid - 1
                
        # 7. Asalu target list lo lekapothe, -1 return chestham
        return -1

# Testing the code
solution = Solution()
print(solution.search([-1, 0, 3, 5, 9, 12], 9))  # Returns 4 (Index of 9)
print(solution.search([-1, 0, 3, 5, 9, 12], 2))  # Returns -1 (2 is not in list)