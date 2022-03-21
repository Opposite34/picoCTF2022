### Current progress: Done

A `disk.img` image file is given.

The prompts asked us to find the key and ssh to it with the following command: 
```
ssh -i key_file -p [PORT] ctf-player@saturn.picoctf.net
```

We have tried the command below to grep all potential PRIVATE KEY files

```bash
strings -t d disk.img | grep -iE "BEGIN (.*) PRIVATE KEY"
```

These are output into [potential_priv_keylist](potential_priv_keylist.txt) 
and tried out each of them by using their offset with [find_offset.py](find_offset.py) to find the offset 
and `ifind` command to find the inode of the files so we could `icat` it out.

However, we seemed to not be able to use any of these keys to login to the server...

### A misunderstanding

It seems like I understood the `ctf-player` part of the prompt wrong -
I thought it was asking for *our* username, but it seems like that it is actually **the** username they need...

The correct key seems to be the one in `/root/.ssh/id_ed25519` - which we found its inode by using `fls -o 206848 disk.img`
(the `206848` is the offset of the sector partition from the `mmls` command).

We then use `fls -o 206848 disk.img [inode]` to go down the file tree for the inode of the key.
The inode of the files are as follow:
- `d/d 470:        root`
- `d/d 3916:       .ssh`
- `r/r 2345:       id_ed25519`

We the `icat -o 206848 disk.img > id_ed25519` to acquired the key and `chmod 400 id_ed25519` the key

After that we ssh into the server with the command:
`ssh -i id_ed25519 -p 49632 ctf-player@saturn.picoctf.net`

We got access to the ssh terminal, which we ran `ls` and found `flag.txt`.
After that, we `cat` the flag out: `picoCTF{k3y_5l3u7h_af277f77}`