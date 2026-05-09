class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = "".join([c for c in s if c.isalnum()])
        string = temp.lower()

        i,j = 0, len(string)-1
        
        while i <= j:
            if string[i] != string[j]:
                return False
            
            i += 1
            j -= 1
        
        return True
