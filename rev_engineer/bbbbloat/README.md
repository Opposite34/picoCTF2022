### Current progress: Done

A `bbbbloat` binary is given. 

Running this prompts `What's my favorite number?` in which we can assume that we need to find the right number to input and it will gives out the flag.

After opening this in ghidra, we went to the `entry` function, which calls `FUN_00101307`
Here's a part of the function:

```
undefined8 FUN_00101307(void)
{
  ...

  local_10 = *(long *)(in_FS_OFFSET + 0x28);
  local_38 = 0x4c75257240343a41;
  local_30 = 0x3062396630664634;
  local_28 = 0x35613066635f3d33;
  local_20 = 0x4e603234363266;
  printf("What\'s my favorite number? ");
  __isoc99_scanf();
  if (local_48 == 0x86187) {
    __s = (char *)FUN_00101249(0,&local_38);
    fputs(__s,stdout);
    putchar(10);
    free(__s);
  }

  ...
}
```

The `scanf` functions put out number into `local_48`, which is then compared to the hex value of `0x86187 (549255)`
If the value is correct, it presumably `fputs` out the flag.

So, we run `bbbbloat` with `549255` as our input and got the flag: `picoCTF{cu7_7h3_bl047_2d7aeca1}`