// HACKERRANK
// https://www.hackerrank.com/challenges/funny-string/problem

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main()
{
    int trials;
    char a[10000],rev[10000];
    scanf("%d",&trials);
    int i;
    for(i=0;i<trials;i++)
    {
        int j,count=0,bol=0;
        scanf("%s",a);
        for(j=0;a[j]!='\0';j++)
            count++;
        for(j=count-1;j>=0;j--)
            rev[count-1-j]=a[j];
        for(j=1;j<count;j++)
        {
            if((fabs((int)a[j]-(int)a[j-1]))!=(fabs((int)rev[j]-(int)rev[j-1])))
            {
                bol=1;
                break;
            }
        }
        if(bol==0)
            printf("Funny\n");
        else
            printf("Not Funny\n");
    }
}
