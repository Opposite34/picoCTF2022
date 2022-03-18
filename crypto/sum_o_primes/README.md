### Current progress: Done

A `gen.py` and its `output.txt` is given.

After searching `sum of primes rsa` on Google, we are met with an interesting interactions on [Stack Exchange](https://crypto.stackexchange.com/questions/87308/relation-between-factors-and-their-sum-on-rsa).

It seems like this can be solved in two ways:
- Solving the quadratic equation `(x-p)(x-q)` since you know both `pq` and `p+q`, this should not be too hard to compute
- Immediately solve for the `d` private key, since we can find `(p-1)(q-1)`

For simplicity in coding. We will be doing the latter.

We made a [solve.py](solve.py) which writes the output into `flag.txt` which gives our flag:
`picoCTF{f5eab190}`