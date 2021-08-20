using System;

namespace fundamentos09
{
    class Program
    {
        static void Main(string[] args)
        {
            //FOREACH
            string[] palavras = {"Maurício", "Alves", "da", "Silva", "Júnior"};

            foreach (string palavra in palavras){
                Console.WriteLine(palavra);
            }

            //FOR

            Console.WriteLine("================================================");
            for(int contador = 0; contador < 10; contador++){
                Console.WriteLine(contador);
                Console.WriteLine("For rodando");
            }

            Console.WriteLine("================================================");
            for(int contador = 0; contador < palavras.Length; contador++){
                Console.WriteLine(palavras[contador]);
            }

            Console.WriteLine("================================================");
            for(int contador2 = palavras.Length - 1; contador2 >= 0; contador2--){
                Console.WriteLine(contador2);
                Console.WriteLine(palavras[contador2]);
            }
            Console.ReadLine();
        }
    }
}
