### Current progress: Done

The `disk.flag.img` which we know contains the flag was given.

First, we ran string on it with the following regex to grap any text file starting with flag in its name.
We then output it to [flag_related.txt](flag_related.txt):
`strings -t d disk.flag.img | grep -iE "flag(.*)txt" > flag_related.txt`

Looking in `flag_related.txt`, we found that `flag.txt` was encrypted with `aes256` and then shredded:
```
219964506 openssl aes256 -salt -in flag.txt -out flag.txt.enc -k unbreakablepassword1234567
219964588 shred -u flag.txt
```
This means we likely have to decrypt the encrypted flag later.


Next we ran the [mmls](http://www.sleuthkit.org/sleuthkit/man/mmls.html) commands, which shows three possible paritions the flag could be:
```
DOS Partition Table
Offset Sector: 0
Units are in 512-byte sectors

...

002:  000:000   0000002048   0000206847   0000204800   Linux (0x83)
003:  000:001   0000206848   0000411647   0000204800   Linux Swap / Solaris x86 (0x82)
004:  000:002   0000411648   0000819199   0000407552   Linux (0x83)
```

From the offset of things we found above, we can determined (by dividing the sectorsize `512` bytes) that
The flag was likely stored in the `411648` offset partition.

So, we ran a recursive [fls](http://www.sleuthkit.org/sleuthkit/man/fls.html) with above offset and grep for the flag:
   `fls -o 411648 -r disk.flag.img | grep flag`
   Which outputs the following:
```
+ r/r * 1876(realloc):  flag.txt
+ r/r 1782:     flag.txt.enc
```

There lies the `flag.txt.enc`. 
So, we used the [icat](https://www.sleuthkit.org/sleuthkit/man/icat.html) command and output it to `flag.txt.enc`:
   `icat -o 411648 disk.flag.img 1782 > flag.txt.enc`

Next, we decrypt the `flag.txt.enc` with the password we found from `flag_related.txt` and output it to `flag.txt`
   `openssl aes256 -d -k unbreakablepassword1234567 -in flag.txt.enc -out flag.txt`

This gives us the flag: `picoCTF{h4un71ng_p457_17237fce}`