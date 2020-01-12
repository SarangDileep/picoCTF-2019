# Handy Shellcode

> The program wants us to pass a shellcode that will redirect us to /bin/sh or in simple words a shellcode that will spawn a shell which has the permissions to read the file flag.txt. So this can be done using the pwntools function shellcraft. As we need the shellcode in assembly we use the asm function to convert it into assembly code. 

> Another way to achieve this is by following the hint given in the challenge description. So a place to find shellcode is [shell-storm](shell-storm.org/shellcode) and find a shellcode which executes /bin/sh and give this as the input of the executable.
