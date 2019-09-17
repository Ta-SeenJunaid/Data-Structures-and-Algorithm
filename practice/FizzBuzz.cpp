/*Write a short program that prints each number from 1 to 100 on a new line. 

For each multiple of 3, print "Fizz" instead of the number. 

For each multiple of 5, print "Buzz" instead of the number. 

For numbers which are multiples of both 3 and 5, print "FizzBuzz" instead of the number.*/

#include <bits/stdc++.h>
using namespace std;




int main()
{
    for(int i=1; i<=100; i++)
    {
        if((i%3 == 0) && (i%5 == 0))
            printf("FizzBuzz\n");

        else if (i%3==0)
            printf("Fizz\n");
        
        else if (i%5==0)
            printf("Buzz\n");

        else
            printf("%d\n",i);
        

    }

}