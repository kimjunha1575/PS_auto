// https://www.acmicpc.net/problem/21758

import java.util.Arrays;
import java.util.Scanner;

public class Main {

	static int N;
	static int[] arr, acc;
	static int ans;
	static int min;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		N = sc.nextInt();
		arr = new int[N];
		acc = new int[N];
		int sum = 0;
		int ans = 0;
		for (int i = 0; i < N; i++) {
			arr[i] = sc.nextInt();
			sum += arr[i];
			acc[i] = sum;
		}
		int tmp;
		tmp = left();
		if (tmp > ans) {
			ans = tmp;
		}
		tmp = right();
		if (tmp > ans) {
			ans = tmp;
		}
		for (int i = 1; i < N - 1; i++) {
			tmp = both(i);
			if (tmp > ans) {
				ans = tmp;
			}
		}

		sc.close();
		System.out.println(ans);
	}

	public static int left() {
		int ret = acc[N - 1] - arr[0];
		int max = 0;
		for (int i = N - 2; i > 0; i--) {
			int tmp = ret - arr[i] + (acc[N - 1] - acc[i]);
			if (tmp > max) {
				max = tmp;
			}
		}
		return max;
	}

	public static int right() {
		int ret = acc[N - 2];
		int max = 0;
		for (int i = 1; i < N - 1; i++) {
			int tmp = ret - arr[i] + (acc[i-1]);
			if (tmp > max) {
				max = tmp;
			}
		}
		return max;
	}

	public static int both(int hive) {
		return (acc[hive] - arr[0]) + (acc[N-2] - acc[hive-1]);
	}
}
// 모두 왼쪽
// 양쪽
// 모두 오른쪽
