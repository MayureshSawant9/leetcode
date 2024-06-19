class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        i_num = 0
        d_num = len(s)
        result = []

        for letter in s:
            if letter == 'I':
                result.append(i_num)
                i_num += 1

            else:
                result.append(d_num)
                d_num -= 1

        if s[-1] == 'I':
            result.append(i_num)
        else:
            result.append(d_num)
        
        return result
        
        