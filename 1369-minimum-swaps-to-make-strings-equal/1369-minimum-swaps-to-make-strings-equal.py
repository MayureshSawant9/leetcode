class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        xy_count = 0
        yx_count = 0

        for letter1, letter2 in zip(s1, s2):
            if letter1 == 'x' and letter2 == 'y':
                xy_count += 1

            elif letter1 == 'y' and letter2 == 'x':
                yx_count += 1 

        if (xy_count + yx_count) % 2:
            return -1
        
        return xy_count // 2 + yx_count // 2 + (xy_count % 2) + (yx_count % 2)