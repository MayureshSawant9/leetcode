class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        #21314
        #2314 
        #2134

        #21413
        #2413
        #2143

        last_seen = None

        for i in range(len(number)):
            if number[i] == digit:
                if i == len(number) - 1:
                    return number[0:-1]
                if number[i+1] > digit:
                    return number[:i] + number[i+1:]

                last_seen = i
        
        return number[:last_seen] + number[last_seen + 1:]
        