#include <stdio.h>

int main()
{

    int index;

    char * nomesAlunos[3][3] = {
        {"Aluno1", "Pt: 30", "Mat: 90"},
        {"Aluno2", "Pt: 60", "Mat: 60"},
        {"Aluno3", "Pt: 90", "Mat: 30"}
    };

    printf("Digite o número do aluno que deseja ver as notas: \n");
    printf("[0] para notas do primeiro aluno \n");
    printf("[1] para notas do segundo aluno \n");
    printf("[2] para notas do terceiro aluno \n");

    scanf("%d", &index);

    printf("A nota do  %s são: %s , %s! \n", nomesAlunos[index][0], nomesAlunos[index][1], nomesAlunos[index][2]);

    return 0;
}