import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        int len;
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        len = Integer.parseInt(br.readLine());
        br.close();
        StringBuilder sb = new StringBuilder();
        for (int i = 1; i <= len; i++) {
            sb.append("*");
            System.out.println(sb);
        }
    }
}