class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}

        for ch in t:
            need[ch] = need.get(ch, 0) + 1

        ans = ""

        for i in range(len(s)):

            if s[i] not in need:
                continue

            temp = need.copy()
            cur = ""

            for r in range(i, len(s)):

                cur += s[r]

                if s[r] in temp:
                    temp[s[r]] -= 1

                    if temp[s[r]] == 0:
                        del temp[s[r]]

                if not temp:
                    if ans == "" or len(cur) < len(ans):
                        ans = cur
                    break

        return ans