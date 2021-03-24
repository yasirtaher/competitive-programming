from typing import List


def restoreString(s: str, indices: List[int]) -> str:
    restored_str = ''
    s_dict = dict(zip(indices, s))
    for i in range(len(s)):
        restored_str += s_dict[i]
    return restored_str


if __name__ == '__main__':
    print(restoreString("codeleet", [4, 5, 6, 7, 0, 2, 1, 3]))
