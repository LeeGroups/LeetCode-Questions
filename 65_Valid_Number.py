def isNumber(self, s: str) -> bool:
    digits = set([str(elem) for elem in range(10)])
    signs = set(["+","-"])
    decimal = False
    e = False
    length = len(s)
    if s[0] in signs:
        if length == 1:
            return False
        else:
            return self.isNumber(s[1:])
    elif s[0] == "." and length == 1:
        return False
    elif s[0] not in digits and s[0] != ".":
        return False
    i = 0
    while i <len(s):
        if s[i] in digits:
            i += 1
        elif s[i] == "e" or s[i] == "E":
            if e:
                return False
            if i + 1 == length:
                return False
            elif s[i+1] in signs:
                if i + 2 == length or s[i+2] not in digits:
                    return False
            elif s[i+1] not in digits:
                return False
            i += 2
            e = True
        elif s[i] == ".":
            if decimal or e:
                return False
            if i == 0 and s[i+1] not in digits:
                return False
            i += 1
            decimal = True
        else:
            return False
    return True