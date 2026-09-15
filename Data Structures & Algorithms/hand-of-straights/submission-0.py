class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        


        cards = Counter(hand)

        hand.sort()

        for n in hand:

            if cards[n]:
                for i in range(n, n + groupSize):
                    if i not in cards:
                        return False
                    cards[i] -= 1
                    if cards[i] == 0:
                        del cards[i]
        
        return True
