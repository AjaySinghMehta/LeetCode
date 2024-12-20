class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        n = len(s)
        l = 0
        r = 0
        char_freq = {}
        max_length = 0

        while r < n:
            char_freq[s[r]] = char_freq.get(s[r], 0) + 1

            while True:
                found = False
                for char, freq in char_freq.items():
                    if freq > 2:
                        found = True
                        char_freq[s[l]] -= 1
                        if char_freq[s[l]] == 0:
                            del char_freq[s[l]]
                        l += 1
                        break
                if not found:
                    break

            max_length = max(max_length, r - l + 1)
            r += 1

        return max_length