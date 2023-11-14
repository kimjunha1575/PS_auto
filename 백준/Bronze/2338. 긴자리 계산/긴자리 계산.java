import java.math.BigInteger;
import java.util.Scanner;

public class Main {
    static BigInteger a, b;
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        a = sc.nextBigInteger();
        b = sc.nextBigInteger();
        sc.close();
        System.out.println(a.add(b));
        System.out.println(a.subtract(b));
        System.out.println(a.multiply(b));
    }
}