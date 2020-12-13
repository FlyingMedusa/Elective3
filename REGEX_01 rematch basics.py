import re

'''
regex is awful and I hate it - Marta 2020

re.match() -> boolean value
metacharacters: [] . ^ $ * + ? {} () \ |
[] - Square brackets - a set of characters you wish to match
[^ab] - any char except a or b
^ - caret - check if a string starts with a certain char
$ - dollar - check if a string ends with a certain char
* - star - matches zero or more occurrences of the pattern left to it
+ - matches one or more occurrences of the pattern left to it
? - question mark - zero or one occurrence of the pattern left to it
{} - braces 
        e.g., {n,m} - at least n, and at most m repetitions of the pattern left to it
| - alternation - or
() - parentheses - group sub-patterns. 
        e.g., (a|b|c)xz match any string that matches either a or b or c followed by xz
\ - backslash - escape various characters including all metacharacters
        e.g., \$a match if a string contains $ followed by a. $ is not interpreted by RegEx in a special way
'''

list_of_words = ["analysis", "abyss", "agents", "alex", "dog", "cat", "beat", "dub", "dumb"]

patterns = ['^a...s$', '[a-p][a-p][a-p]', '[^a]', '^d', '...t$', '..m*b', '..m+b', '..m?b']

print("words:",', '.join(list_of_words))
for pattern in patterns:
    print("WORDS THAT ARE SUITABLE FOR:", pattern)
    for word in list_of_words:      
        result = re.match(pattern, word)
        if result:
            print("   ", word)



