### Current progress: Done

Using the `file` command shows `pico.flag.png: PNG image data, 585 x 172, 8-bit/color RGBA, non-interlaced`
`strings` command doesn't seem to give much information.

After a bit of searching, we come across this [list of steganography tools](https://0xrick.github.io/lists/stego).
We found that for png, `zsteg`. So we ran `zsteg -a pico.flag.png | grep pico` and found this output:

`b1,rgb,lsb,xy       .. text: "picoCTF{7h3r3_15_n0_5p00n_87ef5b0b}$t3g0"`

So the flag is: `picoCTF{7h3r3_15_n0_5p00n_87ef5b0b}`

### Other Resources for more in-depth look
[Tsoding's Hiding Information Inside of PNG](https://youtu.be/M9ZwuIv3xz8)
[PNG's Specification](http://www.libpng.org/pub/png/spec/1.2/PNG-Contents.html)