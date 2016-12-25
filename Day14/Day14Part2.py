import hashlib
import re

salt = 'abc'
salt = 'ihaygndm'

def gen_hash_func(salt, idx):
    gen_salt = salt + str(idx)
    return hashlib.md5(gen_salt).hexdigest()

def extra_hashing(salt, idx):
    gen_salt = gen_hash_func(salt, idx)

    for x in range(2016):
        gen_salt = hashlib.md5(gen_salt).hexdigest()

    return gen_salt

def five_repeats(hash_items, ch):
    byFive = ch * 5

    for it in hash_items:
        if it.find(byFive) != -1:
            return True
    return False

def solve(salt):
    #threes = re.compile(r'(.)\1{2,}')
    threes = re.compile(r'(.)\1\1')
    hash_items = [extra_hashing(salt, i) for i in range(1001)]

    counter = 0
    index = 0

    while True:
        h = threes.search(hash_items.pop(0))
        if h != None and five_repeats(hash_items, h.group(1)):
            counter += 1
            if counter >= 64:
                break

        index += 1
        hash_items.append(extra_hashing(salt, index + 1000)) #len(hash_items)))

    return index

print solve(salt)
#14937 too low
#25622 too high
