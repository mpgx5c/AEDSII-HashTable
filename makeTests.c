

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define Possivel 15

int main(int argc, const char *argv[])
{
    time_t TimeZone;

    if (argc != 4)
    {
        return EXIT_FAILURE;
    }

    int Qtd;
    char *alpha = "abcdefghijklmnopqrstuvwxyz", **String = (char **)calloc(sizeof(char *), atoi(argv[2]));
    char *Oke[] = {"ADD:", "DEL:"};

    FILE *Arquivo = fopen(argv[1], "w");
    srand((unsigned)time(&TimeZone));

    for (int Index = 0; Index < atoi(argv[2]); Index++)
    {
        Qtd = 1 + (rand() % 15);
        String[Index] = (char *)calloc(sizeof(char), Qtd + 5);

        for (int Make = 0; Make < Qtd; Make++)
        {
            String[Index][Make] = (alpha[rand() % 26]);
        }
    }

    srand((unsigned)time(&TimeZone));
    fprintf(Arquivo, "%s\n", argv[3]);
    for (int Percorre = 0; Percorre < atoi(argv[3]); Percorre++)
    {
        Qtd = 1 + rand() % atoi(argv[2]);

        fprintf(Arquivo, "%d\n", Qtd);
        for (int Index = 0; Index < Qtd; Index++)
        {
            fprintf(Arquivo, "%s%s\n", Oke[rand() % 2], String[rand() % atoi(argv[2])]);
        }
    }
    
    fclose(Arquivo);
    free(String);

    return 0;
}