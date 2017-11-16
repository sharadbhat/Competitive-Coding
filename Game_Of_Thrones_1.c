// HACKERRANK
// https://www.hackerrank.com/challenges/game-of-thrones/problem

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main()
{
    char a[100000],alpha[26]={0};
    scanf("%s",a);
    int i,oddcount=0,count=0;
    for(i=0;a[i]!='\0';i++)
        count++;
    for(i=0;i<count;i++)
        alpha[(int)fabs(97-((int)a[i]))]+=1;
    if(count%2==0)
    {
        for(i=0;i<26;i++)
        {
            if((alpha[i])%2!=0)
            {
                printf("NO");
                exit(0);
            }
        }
        printf("YES");
    }
    else if(count%2!=0)
    {
        for(i=0;i<26;i++)
        {
            if((alpha[i])%2!=0)
            {
                if(oddcount==0)
                    oddcount++;
                else if(oddcount==1)
                {
                    printf("NO");
                    exit(0);
                }
            }
        }
        printf("YES");
    }
}
