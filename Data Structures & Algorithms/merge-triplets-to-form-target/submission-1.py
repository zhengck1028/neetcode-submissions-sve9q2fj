class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        cur = [0, 0, 0]
        for tp in triplets:
            if tp[0] <= target[0] and tp[1] <= target[1] and tp[2] <= target[2]:
                cur[0] = max(tp[0], cur[0])
                cur[1] = max(tp[1], cur[1])
                cur[2] = max(tp[2], cur[2])
        return cur == target