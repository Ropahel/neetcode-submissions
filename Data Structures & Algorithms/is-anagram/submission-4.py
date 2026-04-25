class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        dict_t = {}
        for letter in t:
            if letter in dict_t:
                dict_t[letter] += 1
            else:
                dict_t[letter] = 1

        dict_s = {}

        for let in s:
            if let in t:
                if let not in dict_s:
                    dict_s[let] = 1
                else:
                    dict_s[let] += 1
            else:
                return False

        return dict_t == dict_s