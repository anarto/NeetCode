class Solution:
    def isPalindrome(self, text: str) -> bool:
        
        left = 0
        right = len(text) - 1

        while left < right:

            while left < right and not text[left].isalnum():
                left += 1
            
            while right > left and not text[right].isalnum():
                right -= 1

            if left < right:
                if text[left].lower() != text[right].lower():
                    return False
                else:
                    left += 1
                    right -= 1
                
        return True

            