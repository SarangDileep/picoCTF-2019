# SlipperShellcode

> This challenge wants us to give it a shellcode. But there's a twist in this challenge. If you look into the given source code you can see that unlike the last shellcode challenge it jumps to a random location rather than jumping to an exact location. 

> To bypass this we can use ***nop slide***. What it basically does is do no operation until the program branches out at some address. The syscall for a nop is '\x90'. Add 256 nop instruction to the exploit for Handy Shellcode and we will get the flag.
