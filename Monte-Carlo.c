#include<stdio.h>
int main()
{
    int a, r;
    printf("Enter side of square:");
    scanf("%d", &a);
    printf("Enter radius of circle:");
    scanf("%d", &r);
    float pi = 3.14;
    int square;
    float circle;
    square = (2*a) * (2 * a);
    circle = pi * r * r;
    pi = 4 * (circle/square);
    printf("%f", pi);
}