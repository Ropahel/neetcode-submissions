class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        i = 0

        while i < len(temperatures):

            if not stack:
                stack.append(temperatures[i])
                i += 1

            elif stack[-1] >= temperatures[i]:
                stack.append(temperatures[i])
                i += 1

            else:

                continuer = True 
                j = 1

                while continuer:
                    result[i - j] = j
                    stack.pop()
                    
                    if not stack:
                        continuer = False
                    elif stack[-1] >= temperatures[i]:
                        continuer = False
                    else:
                        j += 1
                        while temperatures[i - j] != stack[-1]:
                            j += 1

        return result
