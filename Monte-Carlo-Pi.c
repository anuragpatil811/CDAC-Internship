#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int main()
{
    int i, n, count = 0;
    float x, y;   
    printf("Enter number of iterations: ");
    scanf("%d", &n);
    srand(time(0));
    for(i = 0; i < n; i++) 
    {
        x = (float)rand() / RAND_MAX; 
        y = (float)rand() / RAND_MAX;
        if (x * x + y * y <= 1)
        {
            count++;
        }
    }
    float pi = 4.0 * count / n;
    printf("Approximate value of pi: %f\n", pi);
    return 0;
}
