# OverFlow-1

> On first look of the source code we can see that our input is taken using the gets function which has no buffer size. So buffer overflow is possible. Now let's find out the address of the flag function.To do this let's run the given binary in GDB and do **info functions flag** which will give us the address of flag function as **0x080485e6**. The next step is to change *eip* to this address and to do this we have to find the offset. The input that we give is taken in the function vuln. 

![GDB-vuln](img1.png)

> Here we can see that the address of **ebp-0x48** is loaded into eax and this means that our input is taking 0x48 or 72 bytes. So we have to overflow this part with junk. On the stack after this lies the base pointer which we have to overflow using some junk values. Now lies the instruction pointer or eip. The eip tells the program what is  the next instruction  that has to be taken. So if we put the address of the flag function the program will jump into that function and will execute from there. The address must be given in little endian format as that is the language that the binary understands.

> **Input : *junk to overwrite the buffer + junk to overwrite the ebp + address***
