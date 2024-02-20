import java.util.*;
import java.io.*;

public class Main {
    public static void main(String args[]) throws IOException {
        int left, right;
        String[] input;
        String result;
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        input = br.readLine().split(" ");
        left = Integer.parseInt(input[0]);
        right = Integer.parseInt(input[1]);
        
        if (left < right) {
            result = "<";
        }
        else if (left > right) {
            result = ">";
        }
        else {
            result = "==";
        }
        
        System.out.println(result);
    }
}