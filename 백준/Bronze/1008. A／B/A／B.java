import java.util.Scanner;

public class Main {
    static double a, b;
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        a = sc.nextDouble();
        b = sc.nextDouble();
        sc.close();
        System.out.println(a/b);
    }
}