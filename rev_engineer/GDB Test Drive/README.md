`layout asm` displays `gdbme` in assembly 

`break *(main+99)` sets a breakpoint at the address of main+99

The program stops at the breakpoint and does not execute `<sleep@plt>` which we assumed to be a sleep function

Executing `jump *(main+104)` enabled us to skip the breakpoint and jump straight to the address of `*(main+104)`

The program does not go to sleep and continues running until we reach the address of `<main+125>` which executes `<stdout@@GLIBC_2.2.5>` that gives us `picoCTF{d3bugg3r_dr1v3_93b87433}`

