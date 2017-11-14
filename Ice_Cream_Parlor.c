// HACKERRANK
//

#include<stdio.h>
int main()
{
	int equal, input, value[input];
    int i, j, k, tries;
	scanf("%d", &tries);
	for(i = 1;i <= tries; i++)
	{
		scanf("%d%d", &equal, &input);
		for(j = 0; j < input; j++)
		{
			scanf("%d", &value[j]);
		}
		for(j = 0;j < input; j++)
		{
			for(k = j + 1; k < input; k++)
			{
				if((value[j] + value[k]) == equal)
				printf("%d %d\n", j+1, k+1);
			}
		}
	}
}
