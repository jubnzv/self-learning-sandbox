'''
https://www.codewars.com/kata/make-your-own-hashmap/

This function will take in a list of strings and put them into a hashmap. A hashmap is a quick way to store and lookup items you might need based on the 'hash' of the item (https://en.wikipedia.org/wiki/Hash_table). In this example, we're going to create hashes based on the sum of the characters. Each charater has a decimal value (ascii value) and the sum of those decimal values will be the hash.

Your goal is to take the list of strings, hash them, and return a dictionary with hashes as keys and a list of strings, with that hash, as values.
'''

def my_hash_map(list_of_strings):
    result = {}
    for s in list_of_strings:
        hash = sum([ord(c) for c in s])
        val = result.get(hash)
        if val:
            val.append(s)
            result.update({hash: val})
        else:
            result.update({hash: [s]})

    return result
