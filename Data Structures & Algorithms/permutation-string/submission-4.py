class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:


        if len(s1) > len(s2):
            return False

        d = {}

        for ch in s1:
            d[ch] = d.get(ch, 0) + 1

        for right in range(len(s2) - len(s1) + 1):

            a = d.copy()
            b = s2[right:right + len(s1)]

            c = 0

            while c < len(b):

                if b[c] in a and a[b[c]] > 0:
                    a[b[c]] -= 1

                    if a[b[c]] == 0:
                        del a[b[c]]

                    c += 1
                else:
                    break

            if len(a) == 0 and c == len(b):
                return True

        return False

