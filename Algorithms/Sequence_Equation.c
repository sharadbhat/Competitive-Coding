// HACKERRANK
// https://www.hackerrank.com/challenges/permutation-equation/problem

#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int main()
{
    int n, i, j, k;
    scanf("%d", &n);
    int a[n];
    for(i = 0; i < n; i++)
    {
        scanf("%d", &a[i]);
    }
    for(i = 1; i <= n; i++)
    {
        for(j = 0; j < n; j++)
        {
            if(a[j] == i)
            {
                j++;
                break;
            }
        }
        for(k = 0; k < n; k++)
        {
            if(a[k] == j)
            {
                printf("%d\n", k+1);
                break;
            }
        }
    }
}
