### Current progress: Done

Base upon first look of the file, this seems to be a shell script.
So, we ran the script with `bash Flag.pdf`

Our first output shows the following:
```
x - created lock directory _sh00047.
x - extracting flag (text)
Flag.pdf: line 119: uudecode: command not found
restore of flag failed
flag: MD5 check failed
x - removed lock directory _sh00047.
```

`uudecode` command seems to be missing. 
To fix this, we look into [this askubuntu question](https://askubuntu.com/questions/232440/how-do-i-install-uudecode) and found out that `sharutils` is the package needed.

After that, we got this output once we ran the bash command again
```
x - created lock directory _sh00047.
x - extracting flag (text)
x - removed lock directory _sh00047
``` 

### Many compressions, many pain

We also get a flag file from this. In which, like the challenge suggest, probably needs to find the filetype.
Instead of running `file` command on it, my first thought seems to be to drag this file https://hexed.it/.

The result shows `21 3C 61 72 63 68 3E 0A` - which is the magic number for `ar archiver` in unix.

Running `man ar` shows that we have to use `ar x flag` to extract the file, so we did that.

After that, running the `file` command on it again shows:
`cpio archive`.

So we extracted the `flag` file with `cpio -iv < flag`

We got this output:
```
cpio: flag not created: newer or same age version exists
flag
2 blocks
```

- It seems like `cpio` is trying to create a file called `flag`, but it doesn't want to overwrite our current `flag` file. So let's rename the current `flag` to `flag.cpio` and run the command again.

- The `flag` file given from `flag.cpio` seems to be a `bzip2 compressed data` according to our friend `file` command. To avoid problems with file names again, we rename this file to `flag.bz2` and run `bunzip2 -d flag.bz2`.

- Again, the decompressing the bzip2 file seems to be giving us something new. 
This time, it seems to be `gzip compressed data`. Let's again rename our `flag` file and run `gzip -d flag.gz`

- From that we got an `lzip` file. Renamed the `flag` and run `lzip -d flag.lz`

- Now `LZ4` file. Renamed the `flag` and run `lz4 -d flag.lz4`

- Outputted `lzma` file. Running `lzma -d flag.lzma`

- `lzop` file now. Running `lzop -d flag.lzo`

- We got `lzip` again.

- Then an `xz`

(For those who suggests `binwalk -eM` , we tried. It wasn't able to recurse somehow)


### Finally

We finally got a text file containing 
```
7069636f4354467b66316c656e406d335f6d406e3170756c407431306e5f
6630725f3062326375723137795f35613833373565307d0a
```

Putting this into a hex decoder shows us: `picoCTF{f1len@m3_m@n1pul@t10n_f0r_0b2cur17y_5a8375e0}` our flag.

Just saying that, while this is a seemingly good challenge at first, it is not all that fun that you have to manually
change the file extensions to the decompressing works...