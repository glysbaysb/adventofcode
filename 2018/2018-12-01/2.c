/**
 * freq ranges from -291 to 73940
 * range: 74231
 */
#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <limits.h>

int main() {
	int* seen = calloc(74231, sizeof(int));
	if(seen == NULL) {
		puts("calloc");
		goto EXIT;
	}
	seen[291] = 1;

	int freq = 0;
	char* line = NULL;
	size_t lineLen = 0;
	ssize_t read = 0;
	while(1) {
		FILE* f = fopen("input", "r");
		if(f == NULL) {
			return 1;
		}

		while ((read = getline(&line, &lineLen, f)) != -1) {
			char* endOfLine = NULL;
			long int drift = strtol(line, &endOfLine, 10);

			if(errno || endOfLine == line) {
				goto CLEANUP;
			}

			freq += drift;
			if(seen[freq + 291]) {
				printf("first repeating freq is: %d\n", freq);
				goto CLEANUP;
			}
			seen[freq + 291] = 1;	
		}
		
		fclose(f);
		puts("reopen");
	}

CLEANUP:
	free(line);
EXIT:
	return 0;
}
