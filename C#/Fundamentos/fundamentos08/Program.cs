using System;

namespace fundamentos08
{
    class Program
    {
        static void Main(string[] args)
        {/*
            //WHILE
            int contador = 0;
            while (contador < 10){
                Console.WriteLine(contador);
                contador += 1;
                //contador++ = contador + 1
            }
*/
            // por mais que a condição seja falsa o do while vai executar uma vez
            int contador2 = 0;
            do{
                Console.WriteLine("Do while");
                contador2++;
            } while (contador2 < 10);

            Console.ReadLine();
        }
    }
}
