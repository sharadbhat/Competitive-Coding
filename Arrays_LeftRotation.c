#include <math.h>
#include <stdio.h>
#include <malloc.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>

struct NODE
{
    int val;
    struct NODE *next;
};

typedef struct NODE node;

node *head = NULL;
node *present = NULL;

int main()
{
	int no, rots, i, num;
	scanf("%d%d", &no, &rots);
	
	//TAKING NUMBERS
	for(i = 0; i < no; i++)
	{
		scanf("%d", &num);
		node *temp = head;
		node *newnode = (node *)malloc(sizeof(node));
		newnode->val = num;
		if(head == NULL)
		{
			head = newnode;
			present = head;
		}
		else
		{
			present->next = newnode;
			present = newnode;
		}
		newnode->next = head;
	}
	
	//ROTATION
	for(i = 0; i < rots; i++)
    {
    	head = head->next;
	}
	
	//PRINT
	node *temp = head;
	printf("%d ", temp->val);
	temp = temp->next;
	while(temp != head)
	{
		printf("%d ", temp->val);
		temp = temp->next;
	}
}
