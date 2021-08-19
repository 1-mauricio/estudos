using System;

namespace exercicio02
{
    class Program
    {
        static void Main(string[] args)
        {
            bool fim = false;
            while (fim == false){
                Console.Write("Digite o primeiro número: ");
                int num1 = int.Parse(Console.ReadLine());

                Console.Write("Digite o segundo número: ");
                int num2 = int.Parse(Console.ReadLine());

                float res = num1 % num2;

                if (res == 0){
                    Console.WriteLine(num1);
                } else {
                    Console.WriteLine(res * res);
                }

                Console.Write("Digite zero para parar e qualquer número para continuar: ");
                int continuar = int.Parse(Console.ReadLine());
                if (continuar == 0){
                    fim = true;
                }
            }

            Console.Write("O programa foi finalizado com sucesso");
        }
    }
}
