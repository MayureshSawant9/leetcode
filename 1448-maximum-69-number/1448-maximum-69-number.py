class Solution:
    def maximum69Number (self, num: int) -> int:
        best = -1
        num_str = str(num)
        for index, number in enumerate(num_str):
            if number == '6':
                best = index
                break
        
        else:
            return num

        return int(num_str[:best] + '9' + num_str[best + 1:])
        