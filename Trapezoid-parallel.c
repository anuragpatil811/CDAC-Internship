#include <stdio.h>
#include <omp.h>
double f(double x) 
{
    return x * x;
}
int main() 
{
    long long n;
    printf("Enter number of intervals (max 100000000): ");
    scanf("%lld", &n);
    if (n < 10 || n > 100000000) {
        printf("Invalid input.\n");
        return 1;
    }
    double a = 0.0, b = 1.0;
    double h = (b - a) / n;
    double sum = 0.0;
    double start = omp_get_wtime();
    #pragma omp parallel for reduction(+:sum)
    for (long long i = 1; i < n; i++) 
    {
        double x = a + i * h;
        sum += f(x);
    }
    double result = h * (f(a) + f(b) + 2 * sum) / 2.0;
    double end = omp_get_wtime();
    printf("Integral = %.6f\n", result);
    printf("Execution time = %.2f seconds\n", end - start);
    return 0;
}
