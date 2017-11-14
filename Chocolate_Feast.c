// HACKERRANK
// https://www.hackerrank.com/challenges/chocolate-feast/problem

#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int main()
{
    int total, a, i, n, b, c, m;
    scanf("%d", &a);
    for(i = 0; i < a; i++)
    {
        total = 0;
        scanf("%d%d%d", &n, &c, &m);
        total += n / c;
        b = n / c;
        while(true)
        {
            total += (b / m);
            b = (b / m) +(b % m);
            if(b < m)
            {
                break;
            }
        }
        printf("%d\n", total);
    }
}
