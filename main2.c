#include <time.h>
#include <stdio.h>
#include <fcntl.h>
#include "./test_dir_4/libft.h" //diff

int main ()
{
    int a = 0;
    char *b = "1924823";
    char *c = 0;
    //ft_atoi
    a = ft_atoi(b);
    //ft_itoa
    c = ft_itoa(a);
    free(c);
    printf("DONE");
}
