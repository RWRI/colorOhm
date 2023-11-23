#include <stdio.h>
#include <string.h>

int main(){
   char _,r1[10],r2[10];
   
   float r3,r4;
   
   strcpy(r1,"[r,k,m]");
   strcpy(r2,"[r,k,m]");
   r3 = 200 + 200;
    
   r4 = (1.0/((1.0/200)+1.0/(200)));
    
   printf("r3 = %.2f\n",r3);
   printf("r4 = %.2f\n",r4);
   
   
   return 0;
}