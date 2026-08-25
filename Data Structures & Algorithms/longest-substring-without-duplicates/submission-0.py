class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        longest_sub = 0
        seen = set()          # a set is enough — we only need "is it in the window?"

        for right in range(len(s)):
            # shrink from the left until s[right] is free to add
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])                    # now safe to add
            window_length = right - left + 1
            longest_sub = max(longest_sub, window_length)

        return longest_sub
