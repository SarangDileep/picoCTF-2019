# OverFlow 0

> The main aim of the challenge is to give us an introduction to basic buffer overflows. If we look at the code we can see that we need to cause a segmentation fault which will call the sigsegv_handler function and prints out the flag. You can read more about Buffer overflows [here](https://en.wikipedia.org/wiki/Buffer_overflow).

> The input to the binary should be given as a command line argumnet. So our input should be 
``` python
**./vuln `python -c "print 'a'*136"```**. 
>And this will give us the flag.
