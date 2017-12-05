'''
https://www.codewars.com/kata/bug-squish

Take debugging to a whole new level:

Given a string, remove every *single* bug.

This means you must remove all instances of the word 'bug' from within a given string, *unless* the word is plural ('bugs').

For example, given 'obugobugobuoobugsoo', you should return 'ooobuoobugsoo'.

Another example: given 'obbugugo', you should return 'obugo'.

Note that all characters will be lowercase.

Happy squishing!
'''
import re
debug = lambda s: re.sub(r'(?:bug)+([^s]|$)', r'\1', s)

if __name__ == '__main__':
    print(debug('obugobugobuoobugsoo'))
    print(debug('obbugugo'))
    print(debug('bugs bunny'))
    print(debug('bugs buggy'))
    print(debug('oaiwjefbugoijoijapsbugsdoibugbugjfoijasdfbugsbug'))
