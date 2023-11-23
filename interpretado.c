#include <stdio.h>
#include <string.h>

int main(){
   float r1,r3;
   
   char _,r2[10],r4[10];
   
   r1 = 2200;
   strcpy(r2,"[r,r,m]");
   strcpy(r4,"[r,r,r]");
   r3 = 220;
   printf("r1 = %.2f\n",r1);
   printf("r4 = %s\n",r4);
   
   printf("r2 = %s\n",r2);
   printf("r3 = %.2f\n",r3);
   
   
   return 0;
}