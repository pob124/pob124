

Hello, i'm changhyeon !!!!!!!!
=======
:pray:
=======
where are we?
=======
where are you.
=======
i'm my house.
=======

# pob124

#### notebook message :
###### here is changhyun's notebook

###########what's going on

# C_double_plus_test

ced@ced-virtual-machine:~/바탕화면$ make
gcc -c writeA.c
gcc -o write_only writeA.o writeB.o rnw1.o
gcc -c readA.c
gcc -o read_n_write writeB.o rnw1.o rnw2.o readA.o
gcc -c readB.c
gcc -o readA.o readB.o
/usr/bin/ld: readB.o: warning: relocation against `varAread' in read-only section `.text'
/usr/bin/ld: readB.o: in function `main':
readB.c:(.text+0x5a): undefined reference to `readA'
/usr/bin/ld: readB.c:(.text+0x70): undefined reference to `varAread'
/usr/bin/ld: warning: creating DT_TEXTREL in a PIE
collect2: error: ld returned 1 exit status
make: *** [Makefile:13: read_only] 오류 1
