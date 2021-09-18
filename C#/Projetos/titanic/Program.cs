using System;
using System.IO;

namespace titanic
{
    class Program
    {
        static void Main(string[] args)
        {
            try
            {
                /*
                int qtdHomens = 0;
                int qtdMulheres = 0;
                double media = 0.0;
                int qtd = 0;
                */
                StreamReader sr = File.OpenText("C:\\Workspace\\ESTUDOS\\C#\\Projetos\\titanic\\Titanic.txt");
                StreamWriter sw = new StreamWriter("C:\\Workspace\\ESTUDOS\\C#\\Projetos\\titanic\\sobreviventes.txt");
                string arq = sr.ReadLine();
                while (arq != null)
                {
                    string[] pessoa = arq.Split(',');
                    string sobrevivente = pessoa[1];
                    string nome = pessoa[3];
                    string sexo = pessoa[4];
                    string idade = pessoa[5];
                    Console.WriteLine($"{sobrevivente} {nome} {sexo} {idade}");
                    if (sobrevivente == "1")
                    {   
                        sw.WriteLine($"{nome} {sexo} {idade}");
                        /*
                        qtd += 1;
                        if (sexo == "male")
                        {
                            qtdHomens += 1;
                        }
                        else
                        {
                            qtdMulheres += 1;
                        }
                        media += idade;
                        */
                        
                    }
                    Console.WriteLine(arq);
                }
                //media /= qtd;
            }
            catch (Exception e)
            {
                Console.WriteLine($"Exceção: {e.Message}");
            }
            finally
            {
                Console.WriteLine($"O programa foi finalizado com sucesso.");
                //Console.WriteLine($"A quantidade de homens sobreviventes foi de: {qtdHomens}");
                //Console.WriteLine($"A quantidade de mulheres sobreviventes foi de: {qtdMulheres}");
                //Console.WriteLine($"A média das idades foi de: {media}");
            }
        }
    }
}
