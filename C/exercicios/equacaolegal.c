#include <stdio.h>
#include <stdlib.h>
#include <math.h>

/*

Desenvolva um programa que peça ao usuário um valor de temperatura (T) e de energia
livre padrão (∆G^0). Após isso, peça o um valor para o quociente de reação (Q). Agora o
programa deve indicar se o ∆G é positivo ou negativo, e em cada caso, o que deve ser feito
com o valor de Q, aumentar ou diminuir, para que ∆G= 0. (Dica: utilize a equação abaixo)

∆G = ∆G^0 + RTln(Q)
*/
int main()
{
    float temperatura, elp, quociente, deltag, constanteR;
    constanteR = 0.082;
    
    printf("Insira o valor da temperatura: ");
    scanf("%f", &temperatura);
    
    printf("Insira o valor da energia livre padrão: ");
    scanf("%f", &elp);

    printf("Insira o valor do quociente de reação: ");
    scanf("%f", &quociente);
    
    deltag = elp + constanteR * temperatura * log(quociente);
    
    printf("O valor de DeltaG é igual a: %f\n", deltag);
    
    if (deltag > 0)
    {
        printf("O DeltaG é positivo");
    }
    else if (deltag < 0)
    {
        printf("O DeltaG é negativo");
    }
    
    float mult = constanteR * temperatura;
    float divisao = (elp / mult) * -1;
    float euler = 2.7182818284590452353602874713527;
    float quocienteFinal = pow(euler,divisao);
    
    float result = quocienteFinal - quociente;
    if (result > 0) {
        printf("\no quociente tem que aumentar %f", result);
    } else {
        printf("\no quociente tem que diminuir %f", result);
    }
    
    printf("\n");
    printf("O quociente que mais se aproxima de 0 é: %f", quocienteFinal);
    
    return 0;
}