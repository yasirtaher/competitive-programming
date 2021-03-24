from typing import List


def spellchecker(wordlist: List[str], queries: List[str]) -> List[str]:
    # capitalization
    res = []
    upper_wordlist = [w.upper() for w in wordlist]
    removed_vowel_upper_wordlist = [remove_vowel(w) for w in upper_wordlist]
    for q in queries:
        # When the query exactly matches a word in the wordlist (case-sensitive),
        # you should return the same word back.
        if q in wordlist:
            res.append(q)
        # When the query matches a word up to capitlization, you should return the first such match in the wordlist.
        elif q.upper() in upper_wordlist:
            res.append(wordlist[upper_wordlist.index(q.upper())])
        # When the query matches a word up to vowel errors, you should return the first such match in the wordlist.
        elif remove_vowel(q).upper() in removed_vowel_upper_wordlist:
            res.append(wordlist[removed_vowel_upper_wordlist.index(remove_vowel(q).upper())])
        # If the query has no matches in the wordlist, you should return the empty string.
        else:
            res.append("")
        print(res)
    return res


def remove_vowel(word):
    return "".join('*' if w.lower() in 'aeiou' else w
                   for w in word)


if __name__ == '__main__':
    spellchecker(["KiTe", "kite", "hare", "Hare"],
                 ["kite", "Kite", "KiTe", "Hare", "HARE", "Hear", "hear", "keti", "keet", "keto"])
