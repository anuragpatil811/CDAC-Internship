#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int main() {
    long long int num_points, count_inside = 0;
    double x, y, pi;   
    printf("Enter number of random points: ");
    scanf("%lld", &num_points);
    clock_t start = clock();  
    for (long long int i = 0; i < num_points; i++)
     {
        x = (double)rand() / RAND_MAX;  
        y = (double)rand() / RAND_MAX;
        if ((x * x + y * y) <= 1.0)
        {
            count_inside++;
        }
    }
    pi = 4.0 * count_inside / num_points;
    clock_t end = clock();  
    double time_taken = (double)(end - start) / CLOCKS_PER_SEC;
    printf("Estimated Pi = %.5f\n", pi);
    printf("Execution time = %.2f seconds\n", time_taken);
    return 0;
}
