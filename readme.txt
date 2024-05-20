i'm changhyeon

nice to meet you.

char* perm(mode_t mode) {
   int i;
   static char perms[10];

   strcpy(perms, "---------“);
   for (i=0; i < 3; i++) {
      if (mode & (S_IREAD >> i*3))
         perms[i*3] = 'r';
      if (mode & (S_IWRITE >> i*3))
         perms[i*3+1] = 'w';
      if (mode & (S_IEXEC >> i*3))
         perms[i*3+2] = 'x';
   }
   return(perms);
 }
