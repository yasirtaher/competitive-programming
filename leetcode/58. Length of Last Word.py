def lengthOfLastWord(s: str) -> int:
    # print(len(s))
    if not s.isspace():    
        list =  s.split()
        return(len(list[-1]))
    return 0


print(lengthOfLastWord("Hello World"))
print(lengthOfLastWord(" "))