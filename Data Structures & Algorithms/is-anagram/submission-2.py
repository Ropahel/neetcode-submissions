class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        dict_let_t = {}
        for letter in t:
            if letter in dict_let_t:
                dict_let_t[letter] += 1
            else:
                dict_let_t[letter] = 1

        dict_let_s = {}

        for let in s:
            if let in t:
                if let not in dict_let_s:
                    dict_let_s[let] = 1
                else:
                    dict_let_s[let] += 1
            else:
                return False

        for key in dict_let_t:
            if dict_let_t[key] != dict_let_s[key]:
                return False
                
        return True