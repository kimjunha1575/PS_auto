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

  public static boolean isAns(int N) {
    if (isPalindrome(N) && isPrime(N))
      return true;
    else
      return false;
  }

  public static boolean isPrime(int N) {
    if (N == 1)
      return false;
    for (int i = 2; i <= Math.sqrt(N); i++) {
      if (N % i == 0)
        return false;
    }
    return true;
  }

  public static boolean isPalindrome(int N) {
    String str = Integer.toString(N);
    int len = str.length();
    for (int i = 0; i < len / 2; i++) {
      if (str.charAt(i) != str.charAt(len - i - 1))
        return false;
    }
    return true;
  }
}
