using System;

namespace Training
{   // Loops in c#
    class loops
    {
        static void Main(string[] args)
        {
            Console.WriteLine("For loop");
            for (int i = 0; i < 10; i++)
            {
                Console.WriteLine(i);
            }
            Console.ReadLine();
            
            Console.WriteLine("while loop");
            // Note cannot reuse variable i below, it results in compiler error. It's considered
            // to be in the same scope as i in the for loop.
            int j = 10;
            while (j < 20)
                Console.WriteLine(j++);
            Console.ReadLine();
            
            Console.WriteLine("do while loop");
            do
            {
                Console.WriteLine(j++);
            } while (j < 30);
            Console.ReadLine();
        }
    }
}
