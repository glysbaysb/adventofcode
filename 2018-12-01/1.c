#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <limits.h>

int main() {
	FILE* f = fopen("input", "r");
	if(f == NULL) {
		return 1;
	}

	int max = INT_MIN;
	int min = INT_MAX;

	int counter = 0;
	char* line = NULL;
	size_t lineLen = 0;
	ssize_t read = 0;
	while ((read = getline(&line, &lineLen, f)) != -1) {
		char* endOfLine = NULL;
		long int drift = strtol(line, &endOfLine, 10);

		if(errno || endOfLine == line) {
			goto CLEANUP;
		}

		counter += drift;

		if(max < drift) {
			max = drift;
		}
		if(min > drift) {
			min = drift;
		}
    }

	printf("%d\n", counter);
	printf("drift ranges from %d - %d\n", min, max);

CLEANUP:
	free(line);
	fclose(f);
}
