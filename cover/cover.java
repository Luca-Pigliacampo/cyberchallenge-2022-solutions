import java.util.Scanner;
import java.util.Arrays;

public class cover{
	public static void main(String[] args)
	{
		Scanner in = new Scanner(System.in);

		int N = in.nextInt();
		int K = in.nextInt();
		long[][] ranges = new long[N][2];
		for(long[] r : ranges){
			r[0] = in.nextLong();
			r[1] = in.nextLong();
		}

		System.out.println(conta(N,K,ranges));
	}

	private static long conta(int N, int K, long[][] ranges)
	{
		long[] starts = new long[N];
		long[] ends = new long[N];
		for(int i = 0; i < N; i++){
			starts[i] = ranges[i][0];
			ends[i] = ranges[i][1]+1;
		}
		Arrays.sort(starts);
		Arrays.sort(ends);
		int inds = 0, inde = 0;
		long count = 0, res = 0, change, next, n = starts[0];

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

			change = next - n;
			if(count == K)
				res += change;
			if(n==ends[N-1])
				break;
			n = next;
		}
		return res;
	}
}
