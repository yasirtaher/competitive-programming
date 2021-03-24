def isNumber(s: str) -> bool:
    appear_dot = False
    appear_exp = False
    exp_idx = 0
    dot_idx = 0
    plus_minus = ['+', '-']

    if s == '.':
        return False
    if s[0] == '.' and s[1] == 'e':
        return False
    if s[-1] in plus_minus:
        return False
    if (s[0] in plus_minus) and (not s[1].isdigit()) and len(s) <= 2:
        return False

    if not s[0].isdigit() and (s[0] not in plus_minus) and (s[0] != '.'):
        return False
    else:
        cnt = 1
        for i in s[1:]:
            if not i.isdigit() and (i not in plus_minus):
                if not appear_exp and i.lower() == 'e':
                    appear_exp = True
                    exp_idx = cnt
                elif not appear_dot and i == '.' and s[0] != '.':
                    appear_dot = True
                    dot_idx = cnt
                else:
                    return False
            elif not i.isdigit() and (i in plus_minus):
                if cnt != exp_idx + 1 and appear_exp:
                    return False
                elif (s[0] in plus_minus) and not appear_exp:
                    return False
                elif s[0] not in plus_minus and not appear_exp:
                    return False
            elif not i.isdigit() and i == '.' and (cnt != dot_idx or s[0] == '.'):
                return False

            if appear_exp and appear_dot:
                if dot_idx > exp_idx:
                    return False

            cnt = cnt + 1

        if appear_exp:
            if s[exp_idx - 1] in plus_minus:
                return False

            if exp_idx + 1 == len(s):
                return False
        return True


if __name__ == '__main__':
    # valid
    valid_input_array = [".2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93",
                         "-123.456e789"]

    print("=========valid=======")

    for ia in valid_input_array:
        try:
            print(ia, isNumber(ia))
        except IndexError:
            print(ia)

    # not valid
    invalid_input_array = ["1e.", "2..", "abc", "1a",
                           "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"]
    print("=========invalid=======")
    for ia in invalid_input_array:
        try:
            print(ia, isNumber(ia))
        except IndexError:
            print(ia)
