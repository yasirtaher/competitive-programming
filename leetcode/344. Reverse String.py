from typing import List


def reverseString(s: List[str]) -> None:
    s[:] = s[::-1]
    print(s)


print((reverseString(["h", "e", "l", "l", "o"])))
