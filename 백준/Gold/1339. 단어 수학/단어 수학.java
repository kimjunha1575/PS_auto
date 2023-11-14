import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Collections;
import java.lang.Math;

public class Main {

	private static int N;
	private static String[] words;

	public static void main(String[] args) throws IOException {
		init();
        Alphabet[] arr = new Alphabet[26];
        for (int i = 0; i < 26; i++) {
            arr[i] = new Alphabet((char)('A' + i), 0);
        }
		for (int i = 0; i < N; i++) {
			int len = words[i].length();
			for (int j = 0; j < len; j++) {
                arr[words[i].charAt(j) - 'A'].value += (int)(Math.pow(10, (len-1) - j));
            }
		}
        Arrays.sort(arr, Collections.reverseOrder());

        int idx = 0;
        int ans = 0;
        int num = 9;
        while (arr[idx].value > 0) {
            ans += num-- * arr[idx++].value;
        }
        System.out.println(ans);
	}

	static class Alphabet implements Comparable<Alphabet> {

		public char c;
		public int value;

		public Alphabet(char c, int value) {
			this.c = c;
			this.value = value;
		}

		public int compareTo(Alphabet o) {
			return this.value - o.value;
		}
	}

	public static void init() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		words = new String[N];
		for (int i = 0; i < N; i++) {
			words[i] = br.readLine();
		}
		br.close();
	}
}
