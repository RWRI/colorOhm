#include <stdio.h>
#include <string.h>
int main(){
   float v1;
   
   v1 = 200;
   float v2;
   
   v2 = 200;
   float v3;
   
   v3 = 200;
   float v4;
   
   v4 = (1.0/((1.0/(1.0/((1.0/v1)+1.0/(v2))))+1.0/(v3)));
    
   printf("%f\n",v4);
   
   return 0;
}