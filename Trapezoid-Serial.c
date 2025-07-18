#include <stdio.h>
#include <time.h>
double f(double x)
 {
    return x * x;  //f(x) = x^2
}
int main() 
{
    long long n;
    printf("Enter number of intervals (up to 100000000): ");
    scanf("%lld", &n);
    if (n < 10 || n > 100000000) 
    {
        printf("Invalid input.\n");
        return 1;
    }
    double a = 0.0, b = 1.0;
    double h = (b - a) / n;
    double sum = 0.0;
    clock_t start = clock();  //Records the clock time for execution measurement
    for (long long i = 1; i < n; i++) 
    {
        double x = a + i * h;
        sum += f(x);
    }
    double result = h * (f(a) + f(b) + 2 * sum) / 2.0;
    clock_t end = clock();
    double time = (double)(end - start) / CLOCKS_PER_SEC;
    printf("Integral = %.6f\n", result);
    printf("Execution time = %.2f seconds\n", time);
    return 0;
}
