import java.lang.Math;
import java.util.Arrays;
import java.util.HashSet;

public class Solution {
  static boolean[] visited;
  static int[] nums;
  static HashSet<Integer> primes;

  public int solution(String numbers) {
    nums = new int[numbers.length()];
    visited = new boolean[numbers.length()];
    primes = new HashSet<>();
    Arrays.fill(visited, false);
    for (int i = 0; i < numbers.length(); i++) {
      nums[i] = Integer.parseInt(String.valueOf(numbers.charAt(i)));
    }
    for (int i = 1; i <= numbers.length(); i++) {
      // System.out.println(i + " Start");
      permutation(i, 0, 0);
    }
    return primes.size();
  }

  public static void permutation(int depth, int cur, int length) {
    if (length == depth) {
      // System.out.println(cur);
      if (isPrime(cur)) {
        // System.out.println("Added");
        primes.add(cur);
      }
    } else {
      for (int i = 0; i < nums.length; i++) {
        if (visited[i] == false) {
          visited[i] = true;
          length++;
          int next = cur * 10 + nums[i];
          permutation(depth, next, length);
          visited[i] = false;
          length--;
        }
      }
    }
  }

  public static boolean isPrime(int n) {
    if (n <= 1) return false;
    if (n == 2) return true;
    for (int i = 2; i <= Math.sqrt(n); i++) {
      if (n % i == 0) return false;
    }
    return true;
  }

}
