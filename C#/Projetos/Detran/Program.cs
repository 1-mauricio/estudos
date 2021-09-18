using System;
using System.IO;

namespace test
{
    class Program
    {
        static void Main(string[] args)
        {
            try
            {
                StreamReader sr = File.OpenText("C:\\Workspace\\ESTUDOS\\C#\\Projetos\\Lendo e Gravando txt\\detran.txt");
                StreamWriter sw = new StreamWriter("C:\\Workspace\\ESTUDOS\\C#\\Projetos\\Lendo e Gravando txt\\veicVelhos.txt");
                string arq = sr.ReadLine();
                while (arq != null)
                {
                    string[] linha = arq.Split(' ');
                    string placa = linha[0];
                    string cpf = linha[4];
                    int ano = int.Parse(linha[3]);

                    if (ano <= 2000){
                        sw.WriteLine($"{placa} {ano} {cpf}");
                    }
                    arq = sr.ReadLine();
                }
                sr.Close();
                sw.Close();
            }
            catch (Exception e)
            {
                Console.WriteLine($"Exception: {e.Message}");
            }
            finally
            {
                Console.WriteLine("Programa finalizado com sucesso");
            }
            
        }
    }
}
