### Current progress: not done 

A `game` binary file is given. It is a 64-bit executable that has all the security protections enabled.

According to the challenge description. This is supposedly a dungeon crawler game.
From the hints, it seems like we should:
- Use radare2 instead of ghidra for debugging rather than static analysis. (gdb probably also works, but it's not as powerful).
- Find a way to teleport our characters.