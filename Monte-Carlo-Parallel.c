#include <stdio.h>
#include <stdlib.h>
#include <omp.h>
#include <unistd.h>  
int main() 
{
    long long int num_points;
    printf("Enter number of random points: ");
    scanf("%lld", &num_points);
    long long int count_inside = 0;
    double pi;
    double start = omp_get_wtime();
    omp_set_num_threads(2); 
    #pragma omp parallel
    {
        unsigned int seed = 1234 + omp_get_thread_num();
        long long int local_count = 0;
        double x, y;
        #pragma omp for
        for (long long int i = 0; i < num_points; i++) {

            x = (double)rand_r(&seed) / RAND_MAX;

            y = (double)rand_r(&seed) / RAND_MAX;

            if ((x * x + y * y) <= 1.0)

                local_count++;
        }
        #pragma omp atomic
        count_inside += local_count;
    }
    pi = 4.0 * count_inside / num_points;
    double end = omp_get_wtime();
    printf("PID: %d | Estimated Pi = %.5f | Time = %.6f sec\n", getpid(), pi, end - start);
    return 0;

}

