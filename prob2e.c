/* Problem 2 project Euler, find sum of even Fibonacci numbers < 4,000,000.*/
#include<stdio.h>

int main()
{

    int oldn = 1, newn = 1, temp, sum=0;

    while ( oldn+newn < 4000000 )
    {
        temp = newn;
        newn = oldn+newn;
        oldn = temp;

        if (newn%2==0)
        {
            sum+=newn; // If we hadn't set sum=0, this would give wrong value.
        }

    }

    printf("Answer is %\d",sum);

    return 0;
}

