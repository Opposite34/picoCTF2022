import math
import hashlib
import sys
from tqdm import tqdm
import functools

ITERS = int(2e7)
VERIF_KEY = "96cc5f3b460732b442814fd33cf8537c"
ENCRYPTED_FLAG = bytes.fromhex("42cbbce1487b443de1acf4834baed794f4bbd0dfe58b093b2b84a2c22b")

# This will overflow the stack, it will need to be significantly optimized in order to get the answer :)
@functools.cache
def m_func_og(i):
    if i == 0: return 1
    if i == 1: return 2
    if i == 2: return 3
    if i == 3: return 4

    return 55692*m_func_og(i-4) - 9549*m_func_og(i-3) + 301*m_func_og(i-2) + 21*m_func_og(i-1)

#1st attempt
@functools.cache
def m_func_one(i):
    prev = [1,2,3,4]
    ret_val = 0

    for x in tqdm(range(i-3)):
        ret_val = 55692*prev[0] - 9549*prev[1] + 301*prev[2] + 21*prev[3]
        prev.pop(0)
        prev.append(ret_val)

    return ret_val

# Decrypt the flag
def decrypt_flag(sol):
    sol = sol % (10**10000)
    sol = str(sol)
    sol_md5 = hashlib.md5(sol.encode()).hexdigest()

    if sol_md5 != VERIF_KEY:
        print("Incorrect solution")
        sys.exit(1)

    key = hashlib.sha256(sol.encode()).digest()
    flag = bytearray([char ^ key[i] for i, char in enumerate(ENCRYPTED_FLAG)]).decode()

    print(flag)

if __name__ == "__main__":

    '''
    with open("analyze_mfunc_out.txt", "w") as f:
        for i in range(1, 1001):
            f.write(f"{m_func_og(i)}\n")
    '''

    # x = 1216
    # print(m_func_one(x) == m_func_og(x))

    # sol = m_func(ITERS)
    sol = m_func_one(ITERS)
    decrypt_flag(sol)