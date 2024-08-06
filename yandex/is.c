#include <stdio.h>
#include <stdlib.h>

int signum(int x) {
    if (x > 0) return 1;
    if (x < 0) return -1;
    return 0;
}

int intersects(int a1, int b1, int a2, int b2) {
    return signum(a1 - a2) != signum(b1 - b2);
}

int main() {
    int N;
    scanf("%d", &N);

    int *a = (int *)malloc(N * sizeof(int));
    int *b = (int *)malloc(N * sizeof(int));

    for (int i = 0; i < N; ++i) {
        scanf("%d %d", &a[i], &b[i]);
    }
    int *count = (int *)calloc(N, sizeof(int));

    for (int i = 0; i < N; ++i) {
        for (int j = i + 1; j < N; ++j) {
            if (intersects(a[i], b[i], a[j], b[j])) {
                count[i]++;
                count[j]++;
            }
        }
    }

    int result = 0;
    for (int i = 0; i < N; ++i) {
        if (count[i] == 0) {
            result++;
        }
    }

    printf("%d\n", result);

    free(a);
    free(b);
    free(count);

    return 0;
}
