//usr/bin/env clang -std=c99 -Weverything -lc $0 && ./a.out && rm a.out; exit
#include <sys/stat.h>
#include <fcntl.h>
#include <sys/mman.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

static int is_digit(char c)
{
    return c >= '0' && c <= '9';
}

int main(void)
{
    char *memory = NULL;
    int fd;
    size_t file_size;
    struct stat s;
    char *cursor;

    intmax_t factor1;
    intmax_t factor2;
    intmax_t result = 0;

    fd = open("memory", O_RDONLY);

    if (fd == -1 || fstat(fd, &s)) {
        goto error;
    }

    file_size = (size_t) s.st_size;
    cursor = memory = mmap(NULL, file_size, PROT_READ, MAP_PRIVATE, fd, 0);

    while (cursor < (memory + file_size)) {
        if (*cursor++ == 'm' && *cursor++ == 'u' && *cursor++ == 'l' && *cursor++ == '(') {
            size_t digits = 0;
            intmax_t value = 0;

            while (is_digit(*cursor++) && digits++ < 3) {
                value = value * 10 + *(cursor - 1) - '0';
            }

            if (*(cursor - 1) != ',' || digits < 1 || digits > 3) {
                continue;
            }

            factor1 = value;

            digits = 0;
            value = 0;

            while (is_digit(*cursor++) && digits++ < 3) {
                value = value * 10 + *(cursor - 1) - '0';
            }

            if (*(cursor - 1) != ')' || digits < 1 || digits > 3) {
                continue;
            }

            factor2 = value;
            result += factor1 * factor2;
        }
    }

    printf("Result: %jd\n", result);
    return 0;

error:
    perror("Fatal error");
    return 1;
}
