#include<stdio.h>
long int diffieh(int key,long int root,int primemod)
 {
    int i;
    long int res = 1;
    
    for (i = 0; i < key; i++) {
        res = (res * root) % primemod;
    }
    res = (res + primemod) % primemod;
    return res; 
 }
 
 int main()
 {
  int primemod,keya,keyb,pkeya,pkeyb;
  long int root;
// both the persons will be agreed upon the common n and g  
  printf("Enter the value of root and primemod : ");
  scanf("%ld%d",&root,&primemod);    
// first person will choose the x  
  printf("Enter the private value of pkeya for the first person : ");
  scanf("%d",&pkeya);
  keya=diffieh(pkeya,root,primemod);
  printf("KEYA value is: %d\n", keya);
// second person will choose the y
  printf("Enter the private value of pkeyb for the second person : ");
  scanf("%d",&pkeyb);
  keyb=diffieh(pkeyb,root,primemod);
  printf("KEYB value is: %d\n", keyb);
  printf("key for the first person is : %ld\n",diffieh(pkeya,keyb,primemod));
  printf("key for the second person is : %ld\n",diffieh(pkeyb,keya,primemod));
  return 0;
 }
