### Current progress: not done

A `pin_checker` binary was given. When ran, it asked for 8-digit PIN.

Now, the challenge title and the hints lead us to a `timing attacks`.

We looked into it in detail in [wikipedia](https://en.wikipedia.org/wiki/Timing_attack) and [medium](https://medium.com/spidernitt/introduction-to-timing-attacks-4e1e8c84b32b).

Basically, when cracking a password, one can check the time-taken for the output to be spit out from the program:
- The password usually checks the length first.
- Then, it checks the characters of the password -  one by one.
- If we get a character correct, that means that it proceeds to work on the next character.
- We can infer that the above point is happening due to the time difference that we got from the binary.

We implemented a timing function in python. Using `subprocess` to run shell commands and `timeit` to time our process.
From this, we got the PIN of `48390513`. Checking the PIN with the local `pin_checker` shows that this is the correct PIN.

netcatting to the server and input our PIN gives us the following:
```
Password correct. Here's your flag:
picoCTF{t1m1ng_4tt4ck_0431e830}
```

### Other Resources
[mCoding's video on timing attacks](https://youtu.be/XThL0LP3RjY)