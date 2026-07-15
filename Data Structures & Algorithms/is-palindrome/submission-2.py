class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        
        while left < right:
            # Move the left pointer if it's not alphanumeric
            while left < right and not s[left].isalnum():
                left += 1
            
            # Move the right pointer if it's not alphanumeric
            while left < right and not s[right].isalnum():
                right -= 1
                
            # Compare the characters
            if s[left].lower() != s[right].lower():
                return False  # Mismatch found, definitely not a palindrome
                
            # MUST advance the pointers, or it will infinite loop!
            left += 1
            right -= 1
            
        # If the loop finishes without returning False, it is a palindrome
        return True