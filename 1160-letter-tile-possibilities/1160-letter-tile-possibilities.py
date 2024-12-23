class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        def backtrack(path, remaining_tiles):
            if path:
                result.add(path)
            for i in range(len(remaining_tiles)):
                backtrack(path + remaining_tiles[i], remaining_tiles[:i] + remaining_tiles[i+1:])
        
        result = set()
        backtrack("", sorted(tiles))
        return len(result)

        