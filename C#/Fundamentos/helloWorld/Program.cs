using System;

namespace helloWorld
{
    class Program
    {
        static void Main(string[] args)
        {
            
            var meuTexto = "Hello World - Maurício Alves";

            Console.WriteLine("Hello World!");
            Console.WriteLine(meuTexto);
            
            // int string float bool
            /*
            int segundaGuerraMundial = 1939;
            string cor_favorita = "Vermelho";
            float velocidadeF1 = 294.48f;
            bool segundaGuerraMundialAconteceu = true;

            Console.WriteLine(segundaGuerraMundial);
            Console.WriteLine(cor_favorita);
            Console.WriteLine(velocidadeF1);
            Console.WriteLine(segundaGuerraMundialAconteceu);
            
            velocidadeF1 = 348.29f;
            cor_favorita = "Azul";

            Console.WriteLine(velocidadeF1);
            Console.WriteLine(cor_favorita);
            */
            
            // outra forma de declarar variável
            /*
            var cor_favorita = "Vermelho";
            var modeloDoProduto = 2323;
            */

            // dynamic permite alterar o tipo da variável - não tão recomendado
            /*
            dynamic cor_favorita = "Vermelho";
            Console.WriteLine(cor_favorita);
            cor_favorita = 1231231;
            Console.WriteLine(cor_favorita);
            */

            //imutável
            /*
            const float PI = 3.14159265f;
            */

            Console.ReadLine();

        }
    }
}
