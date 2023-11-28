#include <stdio.h>
#include <string.h>

int main(){
   float r1,r2,r3,rz;
   
   char _,rc[10],rb[10],ra[10];
   
   r1 = 200;
   strcpy(rc,"[m,m,r]");
   r2 = 520;
   strcpy(ra,"[m,g,r]");
   strcpy(rb,"[r,k,m]");
   r3 = r1 + r2;
    
   rz = (1.0/((1.0/(1.0/((1.0/1100)+1.0/(200))))+1.0/(1500)));
    
   printf("r1 = %.2f\n",r1);
   printf("rc = %s\n",rc);
   printf("r2 = %.2f\n",r2);
   printf("ra = %s\n",ra);
   printf("rb = %s\n",rb);
   printf("r3 = %.2f\n",r3);
   printf("rz = %.2f\n",rz);
   
   
   return 0;
}