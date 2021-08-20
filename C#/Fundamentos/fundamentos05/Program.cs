using System;

namespace fundamentos05
{
    class Program
    {
        static void Main(string[] args)
        {
            //ARRAY

            string produto1 = "Sea of thieves";
            string produto2 = "FIFA";
            string produto3 = "Minecraft";
            string produto4 = "Half-life";
            string produto5 = "Portal";
            string produto6 = "CS";
            
            // não pode mudar o tamanho do array
            string[] produtos = new string[5] { 
                "Sea of thieves", 
                "FIFA", 
                "Minecraft", 
                "Half-life",
                "Portal"
            };

            Console.WriteLine(produtos[1]);
            produtos[1] = "FIFA 2021";
            Console.WriteLine(produtos[1]);

            Console.WriteLine(produtos[0]);

            // modo mais simples
            int[] valores = {40, 50, 60, 70, 20};

            Console.WriteLine("Hello World!");
        }
    }
}
