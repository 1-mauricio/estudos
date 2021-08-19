using System;

namespace exercicio01
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Digite um número x: ");
            int x = int.Parse(Console.ReadLine());
            int res = 0;

            if (x%2 == 0){
                res = x * x;
                Console.WriteLine(res);
            }else{
                res = 5 * x;
                Console.WriteLine(res);
            }
        }
    }
}
