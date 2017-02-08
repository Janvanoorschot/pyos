#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <alloca.h>

int main(int argc, char **argv) {
	size_t i=5000;

	if(argc != 4) {
		printf("call as: eatmem <stacksize(Kb)> <heapsize(Kb)> <period(sec)>\n");
		exit(1);
	}
	int stacksize = atoi(argv[1]);
	int heapsize = atoi(argv[2]);
	int period = atoi(argv[3]);


	if(stacksize==0 || heapsize==0 || period==0) {
		printf("error in stacksize, heapsize or period\n");
		exit(2);
	}

	printf("Starting with: stacksize=%d, heapsize=%d, period=%d\n", stacksize, heapsize, period);

	int stackstep = stacksize / period;
	int heapstep = stacksize / period;
	int stackcur = 0;
	int heapcur = 0;
	int curperiod = 0;
	char * buf;

	for(curperiod=0; curperiod < period; curperiod++) {
		buf = (char *) malloc(stackstep*1024);	
		if(buf == NULL) {
			printf("no malloc buf");
			exit(3);
		}
		buf = (char *) alloca(heapstep*1024);
		if(buf == NULL) {
			printf("no alloca buf");
			exit(4);
		}
		sleep(1);
	}

	return 0;
}
