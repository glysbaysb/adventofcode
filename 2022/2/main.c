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
		int desiredOutcome = line[2] - 'X';
		int oppMove = line[0] - 'A';

		int myMove = NULL;

		// draw
		if(desiredOutcome == 1) {
			counter += 3;
			myMove = oppMove;
			printf("draw\n");
		}
		// win
		else if(desiredOutcome == 2) {
			counter += 6;
			printf("win\n");

			if(oppMove == 2) { myMove = 0; }
			else { myMove = oppMove + 1; }
		} else {
			printf("lose\n");
			if(oppMove == 0) { myMove = 2; }
			else { myMove = oppMove - 1; }
		}
		counter += myMove + 1;
	}

	printf("%d", counter);
}

