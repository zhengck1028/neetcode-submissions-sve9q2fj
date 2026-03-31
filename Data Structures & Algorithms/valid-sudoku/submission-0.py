class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        from collections import deque
        bases = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        hashmap = {}
        for i in bases:
            hashmap[i] = deque()
        for r in range(9):
            for c in range(9):
                v = board[r][c]
                if v in bases:
                    hashmap[v].append((r,c))

        # check
        blocks = {
            (0,0):"b1",
            (0,1):"b2",
            (0,2):"b3",
            (1,0):"b4",
            (1,1):"b5",
            (1,2):"b6",
            (2,0):"b7",
            (2,1):"b8",
            (2,2):"b9",
        }
        for b in bases:
            tmp_hm = {"r":[], "c":[], "b":[]}
            while True:
                try:
                    item = hashmap[b].popleft()
                except:
                    break
                row, col = item[0], item[1]
                if row in tmp_hm["r"]:
                    return False
                else:
                    tmp_hm["r"].append(row)
                if col in tmp_hm["c"]:
                    return False
                else:
                    tmp_hm["c"].append(col)
                block = blocks[(row//3, col//3)]
                if block in tmp_hm["b"]:
                    return False
                else:
                    tmp_hm["b"].append(block)
                continue

        return True
