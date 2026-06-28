class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        pairs = {
            '(': ')',
            '[': ']',
            '{': '}'
        }

        for ch in s:
            if ch in pairs:
                stack.append(ch)
            else:
                if not stack:
                    return False

                if pairs[stack[-1]] != ch:
                    return False

                stack.pop()

        return len(stack) == 0