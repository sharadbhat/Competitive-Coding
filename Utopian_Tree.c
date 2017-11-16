// HACKERRANK
// https://www.hackerrank.com/challenges/utopian-tree/problem

#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

int main()
{
    int trials, j, i, h = 1, cycles = 0;
    scanf("%d", &trials);
    for(i = 0;i < trials; i++)
    {
        h = 1;
        scanf("%d", &cycles);
        {
            for(j = 1;j <= cycles; j++)
            {
                if(j % 2 != 0)
                    h = h * 2;
                else
                    h = h + 1;
            }
        }
        printf("%d\n", h);
    }
}
