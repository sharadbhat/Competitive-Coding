// HACKERRANK
// https://www.hackerrank.com/challenges/the-love-letter-mystery/problem

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main()
{
    int trials,non;
    scanf("%d",&trials);
    int i;
    for(i=0;i<trials;i++)
    {
        int total=0,j,no=0,size=10000;
        char a[size];
        scanf("%s",a);
        for(j=0;j<size;j++)
        {
            if((a[j]>=65&&a[j]<=90)||(a[j]>=97&&a[j]<=122))
               no++;
            else
               break;
        }
        non=no;
        if(no%2==0)
        {
            for(j=0;j<=((int)(non/2))-1;j++)
            {
               total+=fabs((int)(a[j])-(int)(a[no-1-j]));
            }
        }
        else
        {
            for(j=0;j<=((int)(non/2));j++)
            {
                total+=fabs((int)(a[j])-(int)(a[no-1-j]));
            }
        }
        printf("%d\n",total);
    }
}
