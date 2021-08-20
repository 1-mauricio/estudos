using System;

namespace fundamentos06
{
    class Program
    {
        static void Main(string[] args)
        {
            // SWITCH

            Console.Write("Escreva o nome da sua cor favorita: ");
            string cor = Console.ReadLine();

            switch(cor){

                case "Vermelho":
                    Console.WriteLine("Sua cor favorita é vermelho");
                    break;
                case "Amarelo":
                    Console.WriteLine("Sua cor favorita é amarelo");
                    break;
                case "Azul":
                    Console.WriteLine("Sua cor favorita é azul");
                    break;
                default: 
                    Console.WriteLine("Sua cor favorita eu não sei");
                    break;
            }


            Console.ReadLine();
        }
    }
}
