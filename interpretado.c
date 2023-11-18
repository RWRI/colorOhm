#include <stdio.h>
#include <string.h>
int main(){
   float v1,v2,v3,v4;
   
   v1 = 200;
   v2 = 200;
   v3 = 100;
   v4 = (1.0/((1.0/(1.0/((1.0/v1)+1.0/(v2))))+1.0/(v3)));
    
   printf("%f\n",v4);
   
   return 0;
}