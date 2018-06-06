// HACKERRANK
// https://www.hackerrank.com/challenges/sparse-arrays/problem

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main()
{
    char a[1000][20]={0};
    char b[1000][20]={0};
    int n,q,j,no,k;
    scanf("%d",&n);
    int i;
    for(i=0;i<n;i++)
        scanf("%s",a[i]);
    scanf("%d",&q);
    for(i=0;i<q;i++)
        scanf("%s",b[i]);
    for(i=0;i<q;i++)
        {
            no=0;
            for(j=0;j<n;j++)
            {
                if(strcmp(b[i],a[j])==0)
                    no++;
            }
            printf("%d\n",no);
        }
}
