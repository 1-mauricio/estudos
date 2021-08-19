using System;

namespace fundamentos03
{
    class Program
    {
        static void Main(string[] args)
        {
            //condicionais
            /*
            int num1 = 39;

            int num2 = 50;

            if (num1>num2)
            {
                Console.WriteLine("o número num1 é maior que o número num2");
            } else if (num1 == num2)
            {
                Console.WriteLine("Os números são iguais");
            }else
            {
                Console.WriteLine("o número 2 é maior que o número 1");
            }

            // &&(e ou and) e ||(ou/or)

            int a = 10;
            int b = 20;
            int c = 200;

            if (a < b || a > c)
            {
                Console.WriteLine("entrou no IF");
            }
            
            //.Parse - converte oq foi digitado em número
            /*
            Console.Write("Digite sua idade: ");
            int idade = int.Parse(Console.ReadLine());

            if (idade >= 0 && idade < 12)
            {
                Console.WriteLine("Você é uma criança!");
            }else if (idade >= 12 && idade <=18)
            {
                Console.WriteLine("Você é um adolescente");
            }else if (idade >= 19 && idade <=60)
            {
                Console.WriteLine("Você é um adulto");
            }else{
                Console.WriteLine("Você é um idoso");
            }
            */
            Console.WriteLine("Comparação de dois números");
            Console.Write("Digite o primeiro número: ");
            int num1 = int.Parse(Console.ReadLine());

            Console.Write("Digite o segundo número: ");
            int num2 = int.Parse(Console.ReadLine());

            if (num1>num2)
            {
                Console.WriteLine("o número " + num1 + " é maior que o número " + num2);
            } else if (num1 == num2)
            {
                Console.WriteLine("Os números são iguais");
            }else
            {
                Console.WriteLine("o número " + num2 + " é maior que o número " + num1);
            }
            Console.ReadLine();
        }
    }
}
