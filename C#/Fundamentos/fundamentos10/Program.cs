using System;

namespace fundamentos10
{
    class Program
    {
        static string meuNomeCompleto = "Maurício Alves da Silva Júnior"; //global

        static void Main(string[] args)
        {
            //ESCOPO
            string meuNome = "Maurício";
            Console.WriteLine(meuNome);//local
            Console.WriteLine(meuNomeCompleto);
        }
        static void ExibirMsg()
        {
            string meuSobrenome = "Alves";
            Console.WriteLine(meuSobrenome);
            Console.WriteLine(meuNomeCompleto);
        }
    }
}
