class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R, C = len(board), len(board[0])
        path = set() # we cannot use same letter twice

        def bt(i, r, c):
            if i == len(word): # meaning we went all the way till end, we found the word
                return True
            
            if (r < 0 or c < 0 # out of bound
                    or
                r >= R or c >= C # out of bound
                    or
                word[i] != board[r][c] # if leter in words is not equal to letter in board
                    or
                (r, c) in path # if row, col already in path
            ):
                return False

            # if we're here, then we know we found matching char

            path.add((r,c))
            res = ( # run bt on all 4 sides, of any retun true, res is true
                    bt(i + 1, r + 1, c)
                        or
                    bt(i + 1, r - 1, c)
                        or 
                    bt(i + 1, r, c + 1)
                        or 
                    bt(i + 1, r, c - 1)
            )

            path.remove((r, c))

            return res
                

        for r in range(R):
            for c in range(C):
                if bt(0, r, c): return True
        return False