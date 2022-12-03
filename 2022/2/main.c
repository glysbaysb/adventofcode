#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <limits.h>

int main() {
	FILE* f = fopen("input", "r");
	if(f == NULL) {
		return 1;
	}

	int counter = 0;
	char* line = NULL;
	size_t lineLen = 0;
	ssize_t read = 0;
	while ((read = getline(&line, &lineLen, f)) != -1) {
		int myMove = line[2] - 'X';
		int oppMove = line[0] - 'A';

		printf("%d %d\t", oppMove, myMove);

		int result = myMove - oppMove;

		// draw
		if(result == 0) {
			counter += 3;
			printf("draw\n");
		}
		// win
		else if(result == 1 || result == -2) {
			counter += 6;
			printf("win\n");
		} else {
			printf("lose\n");
		}
		counter += myMove + 1;
	}

	printf("%d", counter);
}

