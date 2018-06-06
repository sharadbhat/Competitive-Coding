// HACKERRANK
// https://www.hackerrank.com/challenges/angry-professor/problem

#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int main()
{
    int i,trials,tot=0,j,a,min,num;
    scanf("%d",&trials);
    for(i=0;i<trials;i++)
    {
        tot=0;
        scanf("%d%d",&num,&min);
        for(j=0;j<num;j++)
        {
            scanf("%d",&a);
            if(a<=0)
                tot++;
        }
        if(tot<min)
            printf("YES\n");
        else
            printf("NO\n");
    }
}
