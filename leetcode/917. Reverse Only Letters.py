def reverseOnlyLetters(S: str) -> str:
    def insert_str(string, index, char):
        return string[:index] + char + string[index:]
    s_copy = S
    special_char_idx = {}
    for t in range(len(S)):
        if not S[t].isalpha():
            special_char_idx[t] = S[t]
            s_copy = s_copy.replace(S[t], '')
    temp = s_copy[::-1]
    for ch in special_char_idx:
        temp = insert_str(temp, ch, special_char_idx[ch])
    return temp


print(reverseOnlyLetters("ab-cd"))
print(reverseOnlyLetters("a-bC-dEf-ghIj"))
print(reverseOnlyLetters("Test1ng-Leet=code-Q!"))
