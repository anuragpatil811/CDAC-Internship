#include<omp.h>
#include<stdio.h>
int main(int *argc, char *argv[])
{
    #pragma omp parallel
    {
        //Get the total number of OMP threads
        int numt = omp_get_num_threads();
        //Get the thread id of this thread
        int tid = omp_get_thread_num();
        //Print "Hello World" along with thread id and number of threads
        printf("Hello world from threads %d of %d.\n", tid, numt);
    }
    return 0;
}