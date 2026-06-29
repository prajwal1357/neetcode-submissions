class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s=[]
        for i in tokens:
            if i not in {"+", "-", "*", "/"}:
                s.append(i)
            else:
                r=int(eval("".join(reversed([s.pop(),i,s.pop()]))))
                s.append(str(r))
        return int(s[0])