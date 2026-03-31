class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if not hand:
            return False
        hand.sort()
        groups = [[hand[0]]] # [[],[]]
        for i in range(1, len(hand)):
            add = False
            for grp in groups:
                if grp[-1] == hand[i] - 1 and len(grp) < groupSize:
                    grp.append(hand[i])
                    add = True
                    break
            if not add:
                groups.append([hand[i]])
        for grp in groups:
            if len(grp) < groupSize:
                return False
        return True