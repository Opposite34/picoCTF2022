### Current progress: not done

A `sequences.py` is given. In order to get the flag, it seems like we have to run `m_func` with the argument `ITERS` which has a value of `2e7` first.

This to so we can use it in the params which uses the `sha256` of the value to generate the flag:

```py
ITERS = int(2e7)

@functools.cache
def m_func(i):
    if i == 0: return 1
    if i == 1: return 2
    if i == 2: return 3
    if i == 3: return 4

    return 55692*m_func(i-4) - 9549*m_func(i-3) + 301*m_func(i-2) + 21*m_func(i-1)

def decrypt_flag(sol):
    sol = sol % (10**10000)
    sol = str(sol)

    ...

    key = hashlib.sha256(sol.encode()).digest()
    flag = bytearray([char ^ key[i] for i, char in enumerate(ENCRYPTED_FLAG)]).decode()

    print(flag)

if __name__ == "__main__":
    sol = m_func(ITERS)
    decrypt_flag(sol)
```

Since `m_func` is a recursive function, 
we need to find a way to optimize it, otherwise it will causes the call stack to overflow...