using System;

namespace fundamentos04
{
    class Program
    {
        static void Main(string[] args)
        {
            /*
            ExibirMsg();
            GerarPreco(60, "Curso");
            GerarPreco(-20, "Multa");
            GerarValor(50);
            */

            int soma1 = Somar(1, 2, 3);
            int soma2 = Somar(10, 20, 30);
            Console.WriteLine(soma1);
            Console.WriteLine(soma2);
            Console.ReadLine();

        }

        // função: tipo retorno nome()
        // void == retornar nada
        static void ExibirMsg()
        {
            Console.WriteLine("Esse sistmea é bom!");
            Console.WriteLine("Estou usando funções");
            Console.WriteLine("Bem-vindo!");
        }

        static void GerarPreco(int preco, string nome){
            Console.WriteLine("nome do produto: " + nome);
            Console.WriteLine(preco);
        }

        static void GerarValor(int preco){
            //abs = absoluto ou modulo
            int precoAbs = Math.Abs(preco);
            int valorFinal = preco + (2 * preco);
            Console.WriteLine("Valor Final: " + valorFinal);
        }

        //int string bool
        static int Somar(int a, int b, int c){
            int resultadoFinal = a + b + c;
            return resultadoFinal;
        }
    }
}
