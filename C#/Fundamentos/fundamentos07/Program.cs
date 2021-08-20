using System;

namespace fundamentos07
{
    class Program
    {
                //padrão 0 - 1 - 2
        enum Cor { Azul, Verde, Amarelo, Vermelho}

        enum Opcao {Criar = 1, Deletar = 2, Editar = 3, Listar = 4, Atualizar = 5}

        static void Main(string[] args)
        {
            //ENUM
            /*
            Cor corFavorita = Cor.Azul;
            Cor corFavorita2 = Cor.Amarelo;
            Cor corFavoritaDaCarla = Cor.Vermelho;

            Console.WriteLine((int)corFavorita);
            Console.WriteLine((Cor)2);
            Console.WriteLine(corFavoritaDaCarla);
            */
            //MENU

            Console.WriteLine("Selecione uma das opções abaixo: ");
            Console.Write("1-Criar\n2-Deletar\n3-Editar\n4-Listar\n5-Atualizar\n: ");
            int index = int.Parse(Console.ReadLine());
            Opcao opcaoSelecionada = (Opcao)index;

            Console.WriteLine(opcaoSelecionada);

            switch(opcaoSelecionada){
                case Opcao.Criar: 
                    Console.WriteLine("Você quer criar algo");
                    break;
                case Opcao.Deletar:
                    Console.WriteLine("DELETE! DELETE IMEDIATAMENTE");
                    break;
                case Opcao.Editar:
                    Console.WriteLine("Editar é muito bom");
                    break;
                default:
                    Console.WriteLine("Opção não encontrada");
                    break;
            }

            Console.ReadLine();
        }
    }
}
