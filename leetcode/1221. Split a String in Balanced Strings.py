def balancedStringSplit(s: str) -> int:
    l_count, r_count, result = 0, 0, 0
    for ch in s:
        if ch == 'L':
            l_count += 1
        else:
            r_count += 1
        if l_count == r_count:
            result += 1
            l_count, r_count = 0, 0
    return result


print(balancedStringSplit("RLRRRLLRLL"))
