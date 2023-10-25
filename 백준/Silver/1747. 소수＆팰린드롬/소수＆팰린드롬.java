import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
  public static void main(String args[]) throws IOException {
    BufferedReader buf = new BufferedReader(new InputStreamReader(System.in));
    int N = Integer.parseInt(buf.readLine());
    while (isAns(N) == false) {
      N++;
    }
    System.out.println(N);
  }

  private static boolean isAns(int N) { return isPalindrome(N) && isPrime(N); }

  private static boolean isPrime(int N) {
    if (N == 1)
      return false;
    for (int i = 2; i <= Math.sqrt(N); i++) {
      if (N % i == 0)
        return false;
    }
    return true;
  }

  private static boolean isPalindrome(int N) {
    int tmp = N;
    int reverse = 0;
    while (tmp > 0) {
      reverse = reverse * 10 + tmp % 10;
      tmp /= 10;
    }
    return reverse == N;
  }
}
