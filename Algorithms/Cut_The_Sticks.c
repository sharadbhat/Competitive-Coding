// HACKERRANK
// https://www.hackerrank.com/challenges/cut-the-sticks/problem

#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int main()
{
    int num, a[1000], sum = 0, n = 0;
    scanf("%d", &num);
    int i, low;
    for(i = 0; i < num; i++)
        scanf("%d", &a[i]);
    do
    {
        for(i = 0; i < num; i++)
            if(a[i] != 0)
            {
                low = a[i];
                break;
            }
        for(i = 0;i < num; i++)
        {
            if(a[i] <= low && a[i] != 0)
                low = a[i];
        }
        n = 0;
        for(i = 0; i < num; i++)
        {
            if(a[i] != 0)
            {
                a[i] = a[i] - low;
                n++;
            }
        }
        if(n == 0)
        {
            break;
        }
        printf("%d\n", n);
    }while(low != 0);
}
