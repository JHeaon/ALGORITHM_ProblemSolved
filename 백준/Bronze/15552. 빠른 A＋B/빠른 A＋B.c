#include<stdio.h>

int main()
{
	int num = 0;
	int a = 0;
	int b = 0;
	int sum;

	scanf("%d", &num);

	for (int i = 0; i < num; i++)
	{
		scanf("%d %d", &a, &b);
		sum = a + b;
		printf("%d\n", sum);

	}

}