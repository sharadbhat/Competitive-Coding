// HACKERRANK
// https://www.hackerrank.com/challenges/sherlock-and-squares/problem

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main()
{
    int trials,tot;
    unsigned long long start,a,stop,j,i;
    scanf("%d",&trials);
    for(i=0;i<trials;i++)
    {
        tot=0;
        scanf("%llu%llu",&start,&stop);
        for(j=1;j<=(pow(stop,0.5));j++)
        {
            a=j*j;
            if(a>=start&&a<=stop)
                tot++;
        }
        printf("%d\n",tot);
    }
}
