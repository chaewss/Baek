import java.util.Scanner;

public class $10870 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int[] pivot = new int[21];
        if (n <= 20 && n >= 0) {
            pivot[0] = 0;
            pivot[1] = 1;
            for (int i = 2; i <= n; i++) {
                pivot[i] = pivot[i-2] + pivot[i-1];
            }
            System.out.println(pivot[n]);
        }
    }
}
