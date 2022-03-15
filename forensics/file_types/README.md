### Current progress: not done

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

We also get a flag file from this. In which, like the challenge suggest, probably needs to find the filetype.
Instead of running `file` command on it, my first thought seems to be to drag this file https://hexed.it/.

The result shows `21 3C 61 72 63 68 3E 0A` - which is the magic number for `ar archiver` in unix.

Running `man ar` shows that we have to use `ar x flag` to extract the file:
`ar: flag: file format not recognized` - we, however, got this instead