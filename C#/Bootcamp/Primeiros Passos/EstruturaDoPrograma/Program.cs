using System;
using EstruturaDoPrograma.Exemplos;

namespace EstruturaDoPrograma
{
    class Program
    {
        static void Main()
        {
            var Pilha = new Pilha();
            Pilha.Empilha(1);
            Pilha.Empilha(10);
            Pilha.Empilha(100);
            Console.WriteLine(Pilha.Desempilha());
            Console.WriteLine(Pilha.Desempilha());
            Console.WriteLine(Pilha.Desempilha());
        }
    }
}
