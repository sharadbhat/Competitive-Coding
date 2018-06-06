// HACKERRANK
// https://www.hackerrank.com/challenges/lonely-integer/problem

#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int main()
{
    int a[1000] = {0};
    int i, n, b, biggest = 0;
    scanf("%d", &n);
    for(i = 0; i < n; i++)
    {
        scanf("%d", &b);
        if(b > biggest)
        {
            biggest = b;
        }
        a[b]++;
    }
    for(i = 1; i <= biggest; i++)
    {
        if(a[i] == 1)
        {
            printf("%d", i);
            break;
        }
    }
}
