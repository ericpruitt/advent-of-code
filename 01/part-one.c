//usr/bin/env clang -std=c99 -Weverything -lc $0 && ./a.out && rm a.out; exit
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

static int intmax_comparator(const void *a, const void *b)
{
    intmax_t aa = *((const intmax_t *) a);
    intmax_t bb = *((const intmax_t *) b);
    return (aa > bb) - (aa < bb);
}

int main(void)
{
    intmax_t delta;
    FILE *f;
    intmax_t left;
    intmax_t right;

    intmax_t *left_list = NULL;
    size_t list_allocation = 0;
    size_t list_utilization = 0;
    intmax_t result = 0;
    intmax_t *right_list = NULL;

    f = fopen("lists", "r");

    if (!f) {
        goto error;
    }

    while (fscanf(f, "%jd %jd%*1[\n]", &left, &right) != EOF) {
        if (list_allocation == 0 || list_allocation == list_utilization) {
            if (list_allocation == 0) {
                list_allocation = 128;
            } else {
                list_allocation *= 2;
            }

            left_list = realloc(left_list, list_allocation * sizeof(intmax_t));

            if (!left_list) {
                goto error;
            }

            right_list = realloc(right_list, list_allocation * sizeof(intmax_t));

            if (!right_list) {
                goto error;
            }
        }

        left_list[list_utilization] = left;
        right_list[list_utilization] = right;
        list_utilization++;
    }

    fclose(f);

    qsort(left_list, list_utilization, sizeof(intmax_t), intmax_comparator);
    qsort(right_list, list_utilization, sizeof(intmax_t), intmax_comparator);

    for (size_t index = 0; index < list_utilization; index++) {
        delta = labs(left_list[index] - right_list[index]);
        result += delta;
    }

    if (printf("%jd\n", result) < 0) {
        goto error;
    }

    return 0;

error:
    perror("Fatal error");
    return 1;
}
