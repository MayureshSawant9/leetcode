class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        n = len(hand)

        if n % groupSize != 0:
            return False

        count = Counter(hand)
        ref = sorted(hand)

        for element in ref:
            
            if count[element]:
                count[element] -= 1
                
                for i in range(1, groupSize):
                  
                    if count[element + i]:
                        count[element + i] -= 1
                    else:
                        return False
                        
        return True