// HACKERRANK
// https://www.hackerrank.com/challenges/handshake/problem

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main()
{
    int trials;
    scanf("%d",&trials);
    int i;
    for(i=0;i<trials;i++)
    {
        int mem,tot=0,k,j;
        scanf("%d",&mem);
        if(mem==1||mem==0)
            printf("0\n");
        else
        {
            for(k=1;k<mem;k++)
                for(j=k+1;j<=mem;j++)
                    tot++;
            printf("%d\n",tot);
        }
    }
}
