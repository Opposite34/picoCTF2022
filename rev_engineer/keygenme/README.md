### Current progress: not done

A `keygenme` binary is given. This binary is an amd64 little endian executable.
The binary asks for a license key. In which we assume that we need to find the key within the binary.

So we fire up ghidra:
The `entry` function seems to run this `libc_start_main`: 
`__libc_start_main(FUN_0010148b,in_stack_00000000,&stack0x00000008,FUN_00101520,FUN_00101590,param_3,auStack8);`

This should be where we should look into.
Here's the code of the function `FUN_0010148b`:

![FUN_0010148b](fun_1.jpg)

From how its implemented, with the `printf` and the checks and whatnot, for our intents and purposes 
this could be our main function. So, we renamed it as such. 

Seems like it `fgets` 0x25 (37) characters of the input. 
This means we need 36 characters for our flag (last character being `\0` bytes to indicate the end of string)
Then, the value above is passed into `FUN_00101209` function.
This function seems to handle our input and returns `\0` if it's an "invalid key"

In the `FUN_00101209` we found these values:
```c
local_98 = 0x7b4654436f636970;
local_90 = 0x30795f676e317262;
local_88 = 0x6b5f6e77305f7275;
local_80 = 0x5f7933;
local_ba = 0x7d;
```

We realized this is the leetspeak text part of the flag, so we made [join_key](join_key.py) to solve this.
It solves out as `picoCTF{br1ng_y0ur_0wn_k3y_}` which is still an incomplete flag.

We are missing 8 characters (We have 28 characters, so subtract from 36).
It seems like the `FUN_00101209` passes the above values into `MD5` function.
This is probably just an MD5 algorithm, but after that it seems to jumble this all up.

### TODO
- reverse engineer the algorithm OR
- literally just bruteforce it lol (4294967296 possible combinations) (jk that would take 50 days)