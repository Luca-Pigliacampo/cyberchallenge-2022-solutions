#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

static int compara(const void* p1, const void* p2)
{
	if(*(long long int*)p1 < *(long long int*)p2)
		return -1;
	else if(*(long long int*)p1 == *(long long int*)p2)
		return 0;
	else
		return 1;
}

long long int conta(int N, int K, long long int **ranges) {
    // SCRIVI QUA IL TUO CODICE
    long long int* starts = (long long int*)malloc(N*sizeof(long long int));
    long long int* ends = (long long int*)malloc(N*sizeof(long long int));
    for(int i = 0; i<N; i++){
    	starts[i]=ranges[i][0];
	ends[i] = ranges[i][1]+1;
    }
    qsort(starts, N, sizeof(long long int), compara);
    qsort(ends, N, sizeof(long long int), compara);
    long long int inds = 0;
    long long int inde = 0;
    long long int count = 0;
    long long int res = 0;
    long long int change;
    long long int next;
    long long int n = starts[0];
    int percent;
    int lastprc = 0;
    while(n <= ends[N-1]){
	    while(inds<N && n>=starts[inds]){
		    count++;
		    inds++;
	    }
	    while(inde<N && n>=ends[inde]){
		    count--;
		    inde++;
	    }
	    if(inds<N && inde<N)
		    next = starts[inds]<ends[inde]?starts[inds]:ends[inde];
	    else if(inds<N)
		    next = starts[inds];
	    else if(inde<N)
		    next = ends[inde];
	    else
		    next = n;
	    change = next-n;
	    if(count==K){
		    res += change;
	    }
	    if(n == ends[N-1])
		    break;
	    n = next;
    }
    free(starts);
    free(ends);
    return res;
}

int main() {

    // freopen("input.txt", "r", stdin); // DECOMMENTA QUA SE VUOI LEGGERE DA FILE
    // freopen("output.txt", "w", stdout); // DECOMMENTA QUA SE VUOI SCRIVERE DA FILE

    int N, K;
    assert(2 == scanf("%d %d\n", &N, &K));

    long long int **ranges = (long long int **) malloc(N * sizeof(long long int *));

    for(int i=0; i<N; i++) {
       ranges[i] = (long long int *) malloc(2 * sizeof(long long int));
       assert(2 == scanf("%lld %lld\n", &ranges[i][0], &ranges[i][1]));
    }

    printf("%lld\n", conta(N, K, ranges));

    for(int i=0; i<N; i++) {
        free(ranges[i]);
    }
    free(ranges);
    return 0;
}
