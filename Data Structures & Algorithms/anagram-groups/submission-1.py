class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        def is_anagram(s, t):
            if len(s) != len(t):
                return False

            countS, countT = {}, {}

            for i in range(len(s)):
                countS[s[i]] = 1 + countS.get(s[i], 0)
                countT[t[i]] = 1 + countT.get(t[i], 0)
            return countS == countT
        

        list_output = [ [strs[-1]] ]
        strs.pop()

        while strs:
            i = len(list_output) - 1

            while i >= 0 and not is_anagram(strs[-1], list_output[i][0]):
                i -= 1

            if i == -1:
                list_output.append([strs[-1]])
            else:
                list_output[i].append(strs[-1])
            strs.pop()

        return list_output