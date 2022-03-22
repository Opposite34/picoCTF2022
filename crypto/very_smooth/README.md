### Current progress: Done

A `gen.py` and its `output.py` is given.

The challenge name and its hint leads us to `Pollard's p-1 algorithm`.

We read through [Wikipedia](https://en.wikipedia.org/wiki/Pollard%27s_p_%E2%88%92_1_algorithm) and [cs.purdue.edu](https://www.cs.purdue.edu/homes/ssw/cs655/2009f.pdf) articles on this topic, and concludes the following:
- This method works when `p-1` doesn't have that large of a prime factors
- We can give a arbitrary bound to run the program for (in this case, we just give `n`, but theoretically a much smaller number is probably better in practice).

We made a [solve.py](solve.py) which implements the algorithm described.
This script writes the output into `flag.txt`. Running the script gives our flag:
`picoCTF{95d15b05}`

### Some challenges
We spent around an hour or so trying to figure out why we can't get the correct `q` from the `p` we found.
We found out that python's normal division (`/`) operator is imprecised for large number, and the floor division operator (`//`) is to be used instead in these kinds of calculation.